""" Cache Manager

Manipulate cache data by synchronizing with font list directory, gather
information and update  installed font list, gather information about font
updates.

The font structure generated while updating font cache will be,
[{
    id: font_id,
    name: font_name,
    otf: {{
            name: file_name_1.otf,
            cdn: cdn_link,
            sha: latest_sha,
            url: download_link
        }
    }
}]

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 27/11/2016
"""

from cache_manager import Initialize
from consumer import GitHubConsumer
from utility import FileStructure, JsonIO


class Manage:

    def __init__(self):
        self.__structure = FileStructure()

    def update_font_cache(self):
        Initialize().files() # reset cache data json files

        GitHubConsumer("master", "fms-directory", "fontman").download_file(
            self.__structure.list_json(), "list.json"
        )
        font_info_list = []

        for font in JsonIO(self.__structure.list_json()).get_json_as_list():
            font_info = [{"id": font["id"], "name": font["repository"]}]
            consumer = GitHubConsumer(
                font["branch"], font["repository"], font["user"]
            )

            for key, path in font["path_list"][0].items():
                files_list = consumer.list_contents(path)
                font_info[0][key] = []

                for file in files_list:
                    if ".otf" in file["name"]:
                        font_info[0][key].append({
                            "name": file["name"],
                            "cdn": consumer.get_cdn_link(file["path"]),
                            "sha": file["sha"],
                            "url": file["download_url"]
                        })
                font_info_list = font_info_list + font_info

        JsonIO(self.__structure.font_json()).rewrite_json_data(font_info_list)
