""" Font management tools

Access system fonts library and manipulate.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/12/2016
"""

from os import walk
import fontconfig
import os

from consumer import FontsConsumer
from service import FontFaceService
from service import FontFileService
from service import FontService
from service import InstalledFontService
from service import SystemService
from utility import FileManager


def find_files_by_extension(source_dir, extension):
    files_list = []

    for root, dirs, files in walk(source_dir):
        for file in files:
            if file.endswith(extension):
                files_list.append(
                    {
                        "name": file,
                        "file_path": os.path.join(root, file)
                    }
                )

    return files_list


class FontManager:

    def __init__(self):
        self.__system = SystemService().find_system_info()

    def get_system_font_list(self):
        if self.__system.platform in "Windows":
            return os.listdir(os.path.join(os.environ["WINDIR"], "Fonts"))
        else:
            return fontconfig.query()

    def find_by_font_family(self, font_family):
        return fontconfig.query(family=font_family)

    def install_font(self, font_id, rel_id):
        font_dir = "./data/" + font_id
        sys_font_dir = self.__system.font_directory
        sys_fonts_list = self.get_system_font_list()
        artifacts_dir = "./data/" + font_id + "/extracted"

        FileManager().create_directory(artifacts_dir)

        requested_font = FontService().find_by_font_id(font_id).first()

        for font in sys_fonts_list:
            if requested_font.name in font:
                print("Warning! Font already exists")

        if FontService().find_by_font_id(font_id).first().is_installed:
            print("Warning! Font already exists")

        if rel_id in "devel":
            try:
                fontfaces = FontFaceService().find_by_font_id(font_id)

                for fontface in fontfaces:
                    fontfile_name = requested_font.name + "-"\
                                    + fontface.fontface

                    if fontface.download_url.endswith(".otf"):
                        fontfile_name += ".otf"
                    elif fontface.download_url.endswith(".ttf"):
                        fontfile_name += ".ttf"

                    FileManager().download_file(
                        artifacts_dir + "/" + fontfile_name,
                        fontface.download_url
                    )

                fontfiles = find_files_by_extension(font_dir, ".ttf")

                if len(fontfiles) == 0:
                    fontfiles = find_files_by_extension(
                        font_dir, ".otf"
                    )

                if len(fontfiles) == 0:
                    fontfiles = find_files_by_extension(
                        font_dir, ".ufo"
                    )

                print(fontfiles)

                for file in fontfiles:
                    FileManager().move_file(
                        file["name"], sys_font_dir, file["file_path"]
                    )

                    FontFileService().add_new(file["name"], font_id)

                FontService().update_by_font_id(
                    font_id,
                    {
                        "is_installed": True
                    }
                )

                InstalledFontService().add_new(
                    font_id, "devel"
                )
                FileManager().remove_directory(font_dir)

                return True

            except:
                # raise
                return {"error": "Error while installing devel version."}

        release_data = FontsConsumer().consume_rel_info(
            font_id, rel_id
        )

        for asset in release_data["assets"]:
            if "application/zip" in asset["content_type"]:
                FileManager().download_file(
                    font_dir + "/" + asset["name"],
                    asset["browser_download_url"]
                )

                FileManager().extract_file(
                    font_dir + "/" + asset["name"],
                    artifacts_dir
                )

                fontfaces = find_files_by_extension(artifacts_dir, ".ttf")

                if fontfaces is []:
                    fontfaces = find_files_by_extension(
                        artifacts_dir, ".otf"
                    )

                if fontfaces is []:
                    fontfaces = find_files_by_extension(
                        artifacts_dir, ".ufo"
                    )

                for fontface in fontfaces:
                    FileManager().move_file(
                        fontface["name"], sys_font_dir, fontface["file_path"]
                    )
                    FontFileService().add_new(fontface["name"], font_id)

                FontService().update_by_font_id(
                    font_id,
                    {
                        "is_installed": True
                    }
                )

                InstalledFontService().add_new(
                    font_id, release_data["tag_name"]
                )

                FileManager().remove_directory(font_dir)
                return True

            else:
                return {"error": "Please ask maintainer to do a Fontman "
                                 "specific packaging"}

    def remove_font(self, font_id):
        font_files = FontFileService().find_all_by_font_id(font_id)
        sys_font_dir = SystemService().find_system_info().font_directory

        try:
            for file in font_files:
                FileManager().remove_file(sys_font_dir + "/" + file.file_name)

            FontFileService().delete_by_font_id(font_id)
            InstalledFontService().delete_by_font_id(font_id)

            FontService().update_by_font_id(
                font_id,
                {
                    "is_installed": False,
                    "is_upgradable": False
                }
            )

            return True

        except:
            return {"error": "Error while removing font"}
