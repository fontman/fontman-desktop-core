""" Operations

Functions to install, update and remove fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""
import datetime

from service import FontService, InstalledFontService, SystemService
from utility import FileManager


class Operation:

    def install_font(self, font_id):
        file_manager = FileManager()
        font = FontService().find_by_font_id(font_id).one()
        system_information = SystemService().find_system_info()

        system_font_dir = system_information.font_directory
        temp_dir = system_information.fontman_home + '/temp/'
        temp_extracted = temp_dir + "extracted"

        # download font
        file_manager.download_file(
            temp_dir + font.file_name,
            font.url
        )

        # extract zip file
        file_manager.extract_file(temp_dir + font.file_name, temp_extracted)

        # move files to system font directory
        file_manager.move_files(".otf", temp_extracted, system_font_dir)

        # update font installed index
        FontService().update_by_font_id(
            font.font_id,
            {
                "installed": True
            }
        )

        # update Installed Font table
        InstalledFontService().add_new(
            font.font_id,
            datetime.datetime.now(),
            font.version
        )
