""" Cache Manager

Manipulate cache data by synchronizing with font list directory, gather
information and update  installed font list, gather information about font
updates.

The font structure generated while updating font cache will be,
[{
    id: font_id,
    name: font_name,
    files: {
        otf: {
            name: {
                cdn: cdn_link,
                sha: latest_sha,
                url: download_link
            }
        }
    }
}]

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/11/2016
"""

from cache_manager import Index
from consumer import GitHubConsumer
from utility import FileManager, FileStructure, JsonIO


class Manage:

    def __init__(self):
        self.__file_manager = FileManager()
        self.__index = Index()
        self.__structure = FileStructure()
        self.__system = JsonIO(
            self.__structure.system_json()
        ).get_json_as_list()[0]

    def gather_updates(self):
        font_list = JsonIO(
            self.__structure.font_json()
        ).get_json_as_list()

        installed_list = JsonIO(
            self.__structure.installed_json()
        ).get_json_as_list()

        update_list = []
        update = []

        for font in installed_list[0]:
            index = self.__index.find_by_font_id(font["id"])

            installed_info = installed_list[index["installed_index"]]
            font_info = font_list[index["font_index"]]

            # create list considering sha value of a font file
            for key, _list in installed_info["files"]:
                for _key, element in _list:
                    if element["sha"] in font_info[key][_key]["sha"]:
                        continue
                    else:
                        update = [{
                            "id": font["name"],
                            "files": {
                                key: {
                                    _key: {
                                        "sha": font_info[key][_key]["sha"]
                                    }
                                }
                            }
                        }]

            update_list = update_list + update

            # update index.json hash table
            self.__index.update_by_font_id(
                "update_index",
                font["id"],
                update_list.index(update)
            )

        # add a record in update.json
        JsonIO(self.__structure.update_json()).rewrite_json_data(update_list)

    def install_font(self, font_id, type):
        # get font index information
        font_index = self.__index.find_by_font_id(font_id)

        # get font information from font.json
        font_info = JsonIO(
            self.__structure.font_json()
        ).get_json_as_list()[font_index["font_index"]]

        # gather font list to download
        files_list = font_info["files"][type]

        # gather information to write them in installed.json
        installed = [{
            "id": font_info["id"],
            "name": font_info["name"],
            "files": {
                type: {}
            }
        }]

        system_font_directory = JsonIO(
            self.__structure.system_json()
        ).get_json_as_list()[0]["font_directory"]

        # download and install files in system font directory
        for key, file_info in files_list.items():
            self.__file_manager.download_file(
                self.__structure.cached_data_directory() + "/" + key,
                file_info["url"]
            )

            self.__file_manager.move_file(
                key,
                self.__structure.cached_data_directory(),
                system_font_directory
            )

            # add a record in installed list
            installed[0]["files"][type][key] = file_info

        # add the record in installed.json and update hash index
        new_installed_json = JsonIO(
            self.__structure.installed_json()
        ).get_json_as_list() + installed

        JsonIO(self.__structure.installed_json()).rewrite_json_data(
            new_installed_json
        )

        installed_index = (JsonIO(
            self.__structure.installed_json()
        ).get_json_as_list().index(installed[0]))

        self.__index.update_by_font_id(
            "installed_index", font_info["id"], installed_index
        )

    def update_font_cache(self):
        # reset font list, list.json
        GitHubConsumer("master", "fms-directory", "fontman").download_file(
            self.__structure.list_json(), "list.json"
        )
        font_info_list= []
        font_info = []

        # gather font information listed in list.json
        for font in JsonIO(self.__structure.list_json()).get_json_as_list():
            font_info = [{
                "id": font["id"],
                "name": font["repository"],
                "files": {}
            }]
            consumer = GitHubConsumer(
                font["branch"], font["repository"], font["user"]
            )

            for key, path in font["path_list"][0].items():
                files_list = consumer.list_contents(path)
                font_info[0]["files"][key] = {}

                for file in files_list:
                    if ("." + key) in file["name"]:
                        font_info[0]["files"][key][file["name"]] = ({
                            "cdn": consumer.get_cdn_link(file["path"]),
                            "sha": file["sha"],
                            "url": file["download_url"]
                        })
            font_info_list = font_info_list + font_info

            # if font id exists update only the font.json list index
            if self.__index.is_in_index(font["id"]):
                self.__index.update_by_font_id(
                    "font_index",
                    font["id"],
                    font_info_list.index(font_info[0])
                )

            # add a record in index.json
            else:
                self.__index.add_to_index(
                    font["id"],
                    {
                        "font_index": font_info_list.index(font_info[0]),
                        "installed_index": None,
                        "rollback_index": None,
                        "update_index": None
                    }
                )

        # rewrite font.json, font information dictionary
        JsonIO(self.__structure.font_json()).rewrite_json_data(font_info_list)
