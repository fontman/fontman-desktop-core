""" List and get directories/files

Helps to get fms system directory and file paths. Goal is to reduce parsing
home directory and other directory paths as attributes as far as possible.
Each and every method returns a file path or a directory path

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

from os.path import expanduser


class FileStructure:

    def __init__(self):
        self.__home_directory = expanduser('~')

    def cached_data_directory(self):
        return self.__home_directory + '/.fontman/cached_data'

    def fontman_directory(self):
        return self.__home_directory + '/.fontman'

    def font_json(self):
        return self.__home_directory + '/.fontman/repo_data/font.json'

    def home_directory(self):
        return self.__home_directory

    def index_json(self):
        return self.__home_directory + '/.fontman/repo_data/index.json'

    def installed_json(self):
        return self.__home_directory + '/.fontman/repo_data/installed.json'

    def list_json(self):
        return self.__home_directory + '/.fontman/repo_data/list.json'

    def repo_data_directory(self):
        return self.__home_directory + '/.fontman/repo_data'

    def rollback_directory(self):
        return self.__home_directory + '/.fontman/rollback_data'

    def rollback_json(self):
        return self.__home_directory + '/.fontman/rollback_data/rollback.json'

    def system_json(self):
        return self.__home_directory + '/.fontman/system.json'

    def update_json(self):
        return self.__home_directory + '/.fontman/repo_data/update.json'