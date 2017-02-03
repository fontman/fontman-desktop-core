""" Font management tools

Access system font library and manipulate.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/12/2016
"""

from consumer import FontsConsumer
from service import FontFaceService
from service import FontFileService
from service import FontService
from service import InstalledFontService
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
                if font_info[0] in element["name"]:
                    element["fontfaces"].append({
                        "fontface": font_info[1],
                        "resource_path": font["file_path"]
                    })

                    trigger = False
                    break

            if trigger:
                font_data.append({
                    "name": font_info[0],
                    "fontfaces": [{
                        "fontface": font_info[1],
                        "resource_path": font["file_path"]
                    }]
                })

        return font_data

    def install_font(self, font_id, rel_id):
        font_dir = "./data/" + font_id
        sys_font_dir = self.__system.font_directory
        artifacts_dir = "./data/" + font_id + "/extracted"

        FileManager().create_directory(artifacts_dir)

        requested_font = FontService().find_by_font_id(font_id).first()

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

                for file in fontfiles:
                    if "Windows" in self.__system.platform:
                        fixed_install_font(file["file_path"])

                    else:
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
