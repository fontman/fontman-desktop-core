""" Cache Manager

This module covers initializing system, install update fonts, database
manipulation like operations.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from consumer import FontFacesConsumer
from consumer import FontsConsumer
from service import FontFaceService
from service import FontService
from service import InstalledFontService
from service import MetadataService


class CacheManager:

    def add_new_fontfaces(self, new_fontfaces):
        for fontface in new_fontfaces:
            FontFaceService().add_new(
                fontface["fontface_id"],
                fontface["font_id"],
                fontface["fontface"],
                fontface["resource_path"]
            )

    def add_new_font(self, font_id):
        new_font = FontsConsumer().consume_by_font_id(font_id)
        new_fontfaces = FontFacesConsumer().consume_by_query(font_id)

        FontService().add_new(
            new_font["font_id"],
            new_font["name"]
        )

        MetadataService().add_new(
            new_font["metadata_id"],
            new_font["font_id"],
            new_font["default_fontface"],
            new_font["download_url"],
            new_font["license"],
            new_font["version"]
        )

        self.add_new_fontfaces(new_fontfaces)

    def update_font_cache(self):
        update_list = FontsConsumer().consume_all_fonts()

        for font_id in update_list:
            font_data = FontsConsumer().consume_by_font_id(font_id)

            if FontService().is_exists_by_font_id(font_id):
                MetadataService().update_by_font_id(
                    font_id,
                    {
                        "download_url": font_data["download_data"],
                        "version": font_data["version"]
                    }
                )

                installed_font = InstalledFontService().find_by_font_id(font_id)
                if installed_font.first() is not None:
                    if installed_font.version != font_data["version"]:
                        FontService().update_by_font_id(
                            font_id,
                            {
                                "is_upgradable": True
                            }
                        )

                continue

            self.add_new_font(font_id)
