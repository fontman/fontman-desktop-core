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

from utility import FileManager
from utility import FileStructure


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
