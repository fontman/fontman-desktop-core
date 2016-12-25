""" Operations

Functions to install, update and remove fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import datetime
import os
import platform

from service import FontFileService
from service import FontService
from service import InstalledFontService
from service import SystemService
from utility import FileManager

if platform.system() in "Windows":
    import win32api
    import win32con
    import ctypes


class Operation:

    def __init__(self):
        self.__file_manager = FileManager()
        self.__font_files = FontFileService()
        self.__fonts = FontService()
        self.__installed_fonts = InstalledFontService()
        self.__system_info = SystemService().find_system_info()

        self.__system_font_dir = self.__system_info.font_directory
        self.__temp_dir = self.__system_info.fontman_home + '/temp/'
        self.__temp_extracted = self.__temp_dir + "extracted/"

    def download_and_extract(self, font):
        # download font
        self.__file_manager.download_file(
            self.__temp_dir + font.file_name,
            font.url
        )

        # extract zip file
        self.__file_manager.extract_file(
            self.__temp_dir + font.file_name,
            self.__temp_extracted + font.font_id
        )

    def fix_windows_installations(self, file_type, font_id):
        for root, dirs, files in os.walk(self.__temp_extracted + font_id):
            for file in files:
                if file.endswith(file_type):
                    ctypes.windll.gdi32.AddFontResourceA(
                        os.path.join(root, file)
                    )

                    # tracking installed font files
                    self.__font_files.add_new(file, font_id, file_type)

        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE)

    def install(self, file_type, font_id):
        # move files to system font directory
        for root, dirs, files in os.walk(self.__temp_extracted + font_id):
            for file in files:
                if file.endswith(file_type):
                    self.__file_manager.move_file(
                        file, root, self.__system_font_dir
                    )

                    # tracking installed font files
                    self.__font_files.add_new(file, font_id, file_type)

    def install_font(self, font_id):
        font = self.__fonts.find_by_font_id(font_id).one()
        self.download_and_extract(font)

        if self.__system_info.platform in "Windows":
            self.fix_windows_installations("ttf", font.font_id)

        else:
            self.install(".ttf", font.font_id)

        # update font installed index
        self.__fonts.update_by_font_id(
            font.font_id,
            {
                "installed": True

            }
        )

        # update Installed Font table
        self.__installed_fonts.add_new(
            font.font_id,
            datetime.datetime.now(),
            font.version
        )

        return self.return_on_success(font_id)

    def remove_fix_on_windows(self, font_id):
        return

    def remove_font(self, font_id):
        # remove files list
        files_list = self.__font_files.find_all_by_font_id(font_id)

        if self.__system_info.platform in "Windows":
            self.remove_fix_on_windows(font_id)

        else:
            for file in files_list:
                self.__file_manager.remove_file(
                    self.__system_font_dir + "/" + file.file_name
                )

        # clean font cache
        self.__file_manager.remove_directory(
            self.__temp_extracted + "/" + font_id
        )

        # remove font file indexes
        self.__font_files.delete_by_font_id(font_id)

        # remove installed font index
        self.__installed_fonts.delete_by_font_id(font_id)

        # set font installed index and upgradable indexes
        self.__fonts.update_by_font_id(
            font_id,
            {
                "installed": False,
                "upgradable": False
            }
        )

        return True

    def return_on_success(self, font_id):
        status = self.__installed_fonts.find_by_font_id(font_id).one()
        return {
            "font_id": status.font_id,
            "version": status.version
        }

    def update_font(self, font_id):
        # clean font cache
        self.__file_manager.remove_directory(
            self.__temp_extracted + "/" + font_id
        )

        font = self.__fonts.find_by_font_id(font_id).one()
        self.download_and_extract(font)

        # remove old font files index
        self.__font_files.delete_by_font_id(font_id)

        if self.__system_info.platform in "Windows":
            self.fix_windows_installations(".ttf", font_id)
        else:
            # install font files and update font files index
            self.install(".ttf", font_id)

        # update installed fonts version information
        self.__installed_fonts.update_by_font_id(
            font_id,
            {
                "date": datetime.datetime.now(),
                "version": font.version
            }
        )

        # update font upgradable index
        self.__fonts.update_by_font_id(font_id, {"upgradable": False})

        return self.return_on_success(font_id)
