""" Font management tools

Access system font library and manipulate.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/12/2016
"""

from service import FontFileService
from service import FontService
from service import InstalledFontService
from service import MetadataService
from service import SystemService
from utility import FileManager

from os import walk
import os
import platform

if platform.system() in "Windows":
    from utility.win_fix import fixed_install_font


def find_files_by_extension(source_dir, extension):
    files_list = []

    for root, dirs, files in walk(os.path.expanduser(source_dir)):
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

    def get_active_fonts_list(self):
        active_fonts = []
        font_data = []
        fonts_dirs = []

        if self.__system.platform in "Windows":
            fonts_dirs.append(
                os.path.join(os.environ["WINDIR"], "Fonts")
            )

        elif self.__system.platform in "Linux":
            fonts_dirs.append("/usr/share/fonts")

            try:
                fonts_dirs.append(os.path.join("~", ".fonts"))

            except:
                print("No user font directory")

        else:
            fonts_dirs.append(os.path.join("~", "Library/Fonts"))
            fonts_dirs.append("/System/Library/Fonts")

        # list font files in font directories
        for dir in fonts_dirs:
            active_fonts += find_files_by_extension(dir, ".ttf")
            active_fonts += find_files_by_extension(dir, ".otf")

        for font in active_fonts:
            font_info = []

            if "-" in font["name"]:
                font_info = font["name"].split(".")[0].split("-")

            else:
                font_info.append(font["name"].split(".")[0])
                font_info.append("Regular")

            trigger = True

            for element in font_data:
                if font_info[0] == element["name"]:
                    trigger = False
                    break

            if trigger:
                font_data.append({
                    "name": font_info[0],
                    "displayText": font_info[0],
                    "fontface": font_info[0] + "-Regular",
                    "resource_path": font["file_path"]
                })

        return font_data

    def install_font(self, font_id):
        font_dir = "./data/" + font_id
        sys_font_dir = self.__system.font_directory
        artifacts_dir = "./data/" + font_id + "/extracted"
        FileManager().create_directory(artifacts_dir)

        font_data = FontService().find_by_font_id(font_id).first()
        metadata = MetadataService().find_by_font_id(font_id).first()

        FileManager().download_file(
            font_dir + "/" + font_data.name + ".zip",
            metadata.download_url
        )

        FileManager().extract_file(
            font_dir + "/" + font_data.name + ".zip",
            artifacts_dir
        )

        fontfaces = find_files_by_extension(artifacts_dir, ".otf")

        if fontfaces is []:
            fontfaces = find_files_by_extension(
                artifacts_dir, ".ttf"
            )

        print(fontfaces)

        for fontface in fontfaces:
            if "Windows" in self.__system.platform:
                fixed_install_font(fontface["file_path"])

            else:
                FileManager().move_file(
                    fontface["name"],
                    sys_font_dir,
                    fontface["file_path"]
                )

            FontFileService().add_new(fontface["name"], font_id)

        FontService().update_by_font_id(
            font_id,
            {
                "is_installed": True
            }
        )

        InstalledFontService().add_new(
            font_id, metadata.version
        )

        FileManager().remove_directory(font_dir)

        return True

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

    def update_font(self, font_id):
        self.remove_font(font_id)
        self.install_font(font_id)
