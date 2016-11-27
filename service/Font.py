""" Font

Provide services to access font information stored in font cache, designed
for CLI and flask services.
Each and every function returns font information as string, a list or a
dictionary.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/11/2016
"""

from utility import FileStructure, JsonIO


class Font:
    def __init__(self):
        self.__structure = FileStructure()

    def find_all_from_repository(self):
        return JsonIO(self.__structure.list_json()).get_json_as_list()

    def find_info_by_font_id(self, font_id):
        for font in JsonIO(self.__structure.font_json()).get_json_as_list():
            if font_id in font['id']:
                return font

        return None

    def find_installed_by_font_id(self, font_id):
        for item in JsonIO(
                self.__structure.installed_json()
        ).get_json_as_list():
            if font_id in item['id']:
                return item
