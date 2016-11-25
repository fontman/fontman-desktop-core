""" JSON IO

Helps to do CRUD operations on JSON formatted data files.
Uses python json library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import json


class JsonIO:

    def __init__(self, json_file):
        self.__json_file = json_file

    def open_file(self, mode):
        return open(self.__json_file.open, mode)    # modes - r, r+, w, w+...

    def get_json_as_list(self):
        with self.open_file('r') as file_stream:
            return json.load(file_stream)

    def modify_json_data(self, attribute, parent, value):
        json_list = self.get_json_as_list()

        for element in json_list:
            if parent in element:
                element[attribute] = value

        self.rewrite_json_data(json_list)

    def rewrite_json_data(self, json_list):
        with self.open_file('w') as file_stream:
            json.dump(json_list, file_stream)
