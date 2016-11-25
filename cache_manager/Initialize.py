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

from model import FileManager


class Initialize:

    def __init__(self, home_directory):
        self.__file_manager = FileManager(home_directory)

    def proceed(self):
        self.__file_manager.create_directory('cached_data')

        self.__file_manager.create_directory('repo_data')
        self.__file_manager.create_directory('font.json', 'repo_data')
        self.__file_manager.create_file('installed.json', 'repo_data')
        self.__file_manager.create_file('list.json', 'repo_data')

        self.__file_manager.create_directory('rollback_data')
        self.__file_manager.create_file('rollback.json', 'rollback_data')

        self.__file_manager.create_file('system.json')
