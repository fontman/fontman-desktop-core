""" Initialize cache

Initialize cache data locations. Create directory structure to store fms data.

fms_home
|
|----cached_data
|
|----repo_data
|    |----font.json
|    |----installed.json
|    |----list.json
|
|----rollback_data
|    |----rollback.json
|
|----system.json

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import getpass, os, platform

from utility import FileManager, FileStructure, JsonIO


class Initialize:

    def __init__(self):
        self.__file_manager = FileManager()
        self.__structure = FileStructure()

    def directories(self):
        self.__file_manager.create_directory(
            self.__structure.fontman_directory()
        )
        self.__file_manager.create_directory(
            self.__structure.cached_data_directory()
        )
        self.__file_manager.create_directory(
            self.__structure.repo_data_directory()
        )
        self.__file_manager.create_directory(
            self.__structure.rollback_directory()
        )

    def files(self):
        self.__file_manager.create_file(
            self.__structure.font_json()
        )
        self.__file_manager.create_file(
            self.__structure.index_json()
        )
        self.__file_manager.create_file(
            self.__structure.installed_json()
        )
        self.__file_manager.create_file(
            self.__structure.list_json()
        )
        self.__file_manager.create_file(
            self.__structure.rollback_json()
        )
        self.__file_manager.create_file(
            self.__structure.system_json()
        )
        self.__file_manager.create_file(
            self.__structure.update_json()
        )

    def system_settings(self):
        font_dir = ""
        system = platform.system()

        if "linux" in system.lower():
            font_dir = self.__structure.home_directory() + "/.fonts"
        elif "osx" in system.lower():
            font_dir = self.__structure.home_directory() + "/Library/Fonts"
        elif "windows" in system.lower():
            font_dir = os.environ["SYSTEMDRIVE"] + "\\\\Windows\\Fonts"

        system_info_list = [{
            "font_directory": font_dir,
            "refresh": 2,
            "system": platform.system(),
            "username": getpass.getuser()
        }]

        JsonIO(
            self.__structure.system_json()
        ).rewrite_json_data(system_info_list)
