""" Index

Font index, data gathering to decrease search time.
This class stores data in in repo_date/update.json as a json hash map.

Hash map structure,
[
    {
        font_id: {
            font_index: 1,
            installed_index: 0,
            rollback_index: 1,
            update_index: 1
        }
    }
]

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/11/2016
"""

from utility import FileStructure, JsonIO


class Index:

    def __init__(self):
        self.__jsonIO = JsonIO(FileStructure().index_json())

    def add_to_index(self, font_id, index_info):
        index_list = self.__jsonIO.get_json_as_list()

        if len(index_list) is 0:
            index_list.append({})

        index_list[0][font_id] = index_info
        self.__jsonIO.rewrite_json_data(index_list)

    def find_all(self):
        return self.__jsonIO.get_json_as_list()

    def find_by_font_id(self, font_id):
        try:
            return self.__jsonIO.get_json_as_list()[0][font_id]
        except:
            return None

    def is_in_index(self, font_id):
        try:
            if self.__jsonIO.get_json_as_list()[0][font_id]:
                return True
        except:
            return False

    def update_by_font_id(self, element, font_id, value):
        index_list = self.__jsonIO.get_json_as_list()
        index_list[0][font_id][element] = value

        self.__jsonIO.rewrite_json_data(index_list)
