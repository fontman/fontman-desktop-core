""" Operations

Functions to install, update and remove fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import datetime, os

from service import FontFileService, FontService, InstalledFontService, \
    SystemService
from utility import FileManager


class Operation:

    def __init__(self):
        self.__file_manager = FileManager()
        self.__font_files = FontFileService()
        self.__fonts = FontService()
        self.__installed_fonts = InstalledFontService()
        self.__system_info = SystemService().find_system_info()

        self.__system_font_dir = self.__system_info.font_directory
        self.__temp_dir = self.__system_info.fontman_home + '/temp/'
        self.__temp_extracted = self.__temp_dir + "extracted"

    def download_and_extract(self, font):
        # download font
        self.__file_manager.download_file(
            self.__temp_dir + font.file_name,
            font.url
        )

        # extract zip file
        self.__file_manager.extract_file(
            self.__temp_dir + font.file_name, self.__temp_extracted
        )

    def install(self, file_type, font_id, version):
        # move files to system font directory
        for root, dirs, files in os.walk(self.__temp_extracted):
            for file in files:
                if file.endswith(".otf"):
                    self.__file_manager.move_file(
                        file, root, self.__system_font_dir
                    )

                    # tracking installed font files
                    self.__font_files.add_new(file, font_id, version)

    def install_font(self, font_id):
        font = self.__fonts.find_by_font_id(font_id).one()
        self.download_and_extract(font)
        self.install(".otf", font.font_id, font.version)

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

        # clean workspace directories
        self.__file_manager.remove_directory(self.__temp_extracted)
        self.__file_manager.remove_directory(self.__temp_dir + font.file_name)

    def remove_font(self, font_id):
        # remove files list
        files_list = self.__font_files.find_all_by_font_id(font_id)

        for file in files_list:
            self.__file_manager.remove_file(
                self.__system_font_dir + "/" + file.file_name
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
        
    def update_font(self, font_id):
        font = self.__fonts.find_by_font_id(font_id).one()
        self.download_and_extract(font)

        # install font files and update font files index
        self.__font_files.delete_by_font_id(font_id)
        self.install(".otf", font_id, font.version)

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

        # clean workspace directories
        self.__file_manager.remove_directory(self.__temp_extracted)
        self.__file_manager.remove_directory(self.__temp_dir + font.file_name)
