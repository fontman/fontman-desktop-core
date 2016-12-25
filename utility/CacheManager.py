""" Cache Manager

This module covers initializing system, install update fonts, database
manipulation like operations.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""
from consumer import FontmanConsumer
from service import ChannelService
from service import FontLanguageService
from service import FontService
from service import FontStyleService
from service import LanguageService


class CacheManager:

    def __init__(self):
        self.__channels = ChannelService()
        self.__consumer = FontmanConsumer()
        self.__fonts = FontService()
        self.__font_languages = FontLanguageService()
        self.__font_styles = FontStyleService()
        self.__languages = LanguageService()

    def refresh_cache(self):
        channels = self.__consumer.get_all_channels()
        fonts = self.__consumer.get_all_fonts()
        font_languages = self.__consumer.get_all_font_languages()
        font_styles = self.__consumer.get_all_font_styles()
        languages = self.__consumer.get_all_languages()

        # update channels list
        for channel in channels:
            if self.__channels.is_exists_by_id(channel["channel_id"]):
                continue

            else:
                self.__channels.add_new(
                    channel["channel_id"], channel["name"], channel["type"]
                )

        # upgrade fonts list
        for font in fonts:
            if self.__fonts.is_exists_by_font_id(font["font_id"]):
                _font = self.__fonts.find_by_font_id(font["font_id"])

                if _font.version not in font["version"]:
                    self.__fonts.update_by_font_id(
                        font["font_id"],
                        {
                            "version": font["version"]
                        }
                    )

                    if _font.instlled:
                        self.__fonts.update_by_font_id(
                            font["font_id"],
                            {
                                "upgradable": True
                            }
                        )

                continue

            else:
                self.__fonts.add_new(
                    font["font_id"],
                    font["channel_id"],
                    font["name"],
                    font["preview_cdn"],
                    font["sample"],
                    font["type"],
                    font["url"],
                    font["version"]
                )

        for style in font_styles:
            if self.__font_styles.is_exists_by_style_id(style["id"]):
                continue

            else:
                self.__font_styles.add_new(
                    style["id"], style["cdn"], style["font_id"], style["style"]
                )

        for language in languages:
            if self.__languages.is_exists_by_id(language["id"]):
                continue
            else:
                self.__languages.add_new(
                    language["id"], True, language["value"]
                )

        for font_language in font_languages:
            if self.__font_languages.is_exists_by_id(font_language["id"]):
                continue
            else:
                self.__font_languages.add_new(
                    font_language["id"],
                    font_language["font_id"],
                    font_language["language_id"]
                )
