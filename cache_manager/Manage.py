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
from utility import FileStructure, JsonIO


class Manage:

    def __init__(self):
        self.__index = Index()
        self.__structure = FileStructure()

    def list_updates(self):
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
            self.__index.update_by_font_id(
                "update_index",
                font["id"],
                update_list.index(update)
            )

        JsonIO(self.__structure.update_json()).rewrite_json_data(update_list)


    def update_font_cache(self):
        # reset font list, font.json
        GitHubConsumer("master", "fms-directory", "fontman").download_file(
            self.__structure.list_json(), "list.json"
        )
        font_info_list= []
        font_info = []

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

            if self.__index.is_in_index(font["id"]):
                self.__index.update_by_font_id(
                    "font_index",
                    font["id"],
                    font_info_list.index(font_info[0])
                )
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

        JsonIO(self.__structure.font_json()).rewrite_json_data(font_info_list)
