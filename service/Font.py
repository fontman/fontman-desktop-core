""" Font

Provide services to access font information stored in font cache, designed
for CLI and flask services.
Each and every function returns font information as boolean, string, a list or a
dictionary.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/11/2016
"""

from cache_manager import Index
from utility import FileStructure, JsonIO


class Font:
    def __init__(self):
        self.__index = Index()
        self.__structure = FileStructure()

    def find_all(self):
        return JsonIO(self.__structure.font_json()).get_json_as_list()

    def find_info_by_font_id(self, font_id):
        return JsonIO(
            self.__structure.font_json()
        ).get_json_as_list()[
            self.__index.find_by_font_id(font_id)["font_index"]
        ]

    def is_installed(self, font_id):
        if self.__index.find_by_font_id(font_id)["installed_index"] is None:
            return False
        else:
            return True

    def is_upgradable(self, font_id):
        if self.__index.find_by_font_id(font_id)["update_index"] is None:
            return False
        else:
            return True
