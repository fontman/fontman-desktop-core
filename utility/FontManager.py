""" Font management tools

Access system fonts library and manipulate.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/12/2016
"""

from os import walk
import fontconfig
import os

from consumer import FontsConsumer
from service import FontFileService
from service import FontService
from service import InstalledFontService
from service import SystemService
from utility import FileManager


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

    def find_files_by_extension(self, source_dir, extension):
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

    def install_font(self, font_id, rel_id):
        requested_font = FontService().find_by_font_id(font_id).first()
        sys_fonts_list = self.get_system_font_list()

        for font in sys_fonts_list:
            if requested_font.name in font:
                return {"error": "Font has been already installed"}

        release_data = FontsConsumer().consume_rel_info(
            font_id, rel_id
        )

        for asset in release_data["assets"]:
            if "application/zip" in asset["content_type"]:
                artifacts_dir = "./data/" + font_id + "/extracted"
                font_dir = "./data/" + font_id
                sys_font_dir = self.__system.font_directory

                FileManager().create_directory(artifacts_dir)
                FileManager().download_file(
                    font_dir + "/" + release_data["name"],
                    release_data["browser_download_url"]
                )

                FileManager().extract_file(
                    font_dir + "/" + release_data["name"],
                    artifacts_dir
                )

                fontfaces = self.find_files_by_extension(artifacts_dir, ".ttf")

                if fontfaces is []:
                    fontfaces = self.find_files_by_extension(
                        artifacts_dir, ".otf"
                    )

                if fontfaces is []:
                    fontfaces = self.find_files_by_extension(
                        artifacts_dir, ".ufo"
                    )

                for fontface in fontfaces:
                    FileManager().move_file(
                        fontface["name"], sys_font_dir, fontface["file_path"]
                    )
                    FontFileService().add_new(fontface["name"], font_id)

                InstalledFontService().add_new(
                    font_id, release_data["tag_name"]
                )

                return {"success": "Font successfully installed"}

            else:
                return {"error": "Please ask maintainer to do a Fontman "
                                 "specific packaging"}
