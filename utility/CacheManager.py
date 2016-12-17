""" Cache Manager

This module covers initializing system, install update fonts, database
manipulation like operations.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import requests

from consumer import GitHubConsumer
from service import ChannelService, FontLanguageService, FontService, \
    GitHubFontService, GitLabFontService, LanguageService, WebLinkService


class CacheManager:

    def __init__(self):
        self.__channel_service = ChannelService()
        self.__font_languages = FontLanguageService()
        self.__font_service = FontService()
        self.__github_fonts = GitHubFontService()
        self.__gitlab_fonts = GitLabFontService()
        self.__languages = LanguageService()

    def update_font_cache(self):
        channels = self.__channel_service.find_all()

        for channel in channels:
            # skip if channel is disabled
            if not channel.is_active:
                continue

            if "github" in channel.type:
                self.update_github_based_channel(channel)

    def update_github_based_channel(self, channel):
        # get fonts list from channel
        fonts_list = requests.get(channel.base_url).json()

        # update fonts information
        for font in fonts_list:
            if "github" in font["type"]:
                self.update_github_font(channel.channel_id, font)
            elif "gitlab" in font["type"]:
                self.update_gitlab_font()

    def update_github_font(self, channel_id, font):
        # get font data using github API
        latest_release = GitHubConsumer(
            font["style_branch"], font["repository"], font["user"]
        ).get_latest_release_info()
        release_info = None

        for asset in latest_release["assets"]:
            if asset["content_type"] in "application/zip":
                release_info = asset
                break

        # update font data if font already exists
        font_obj = self.__font_service.find_by_font_id(font["id"])

        if font_obj.count() is not 0:
            font_obj = font_obj.one()

            # check for version updates
            if font_obj.installed:
                if font_obj.version not in latest_release["tag_name"]:
                    self.__font_service.update_by_font_id(
                        font["id"],
                        {
                            "file_name": release_info["name"],
                            "upgradable": True,
                            "url": release_info["browser_download_url"],
                            "version": latest_release["tag_name"]
                        }
                    )
                return

        # add a record in fonts directory
        self.__font_service.add_new(
            font["id"],
            channel_id,
            release_info["name"],
            font["name"],
            font["style_regular"],
            font["sample"],
            font["type"],
            release_info["browser_download_url"],
            latest_release["tag_name"]
        )

        # update languages data
        for value in font["languages"]:
            self.update_language_data(font["id"], value)

        # add a detailed infromation record in github fonts table
        self.__github_fonts.add_new(
            font["id"],
            font["repository"],
            font["style_branch"],
            font["style_path"],
            font["user"]
        )

        # generate cdn links using provided branch(probably gh-pages)
        consumer = GitHubConsumer(
            font["style_branch"],
            font["repository"],
            font["user"]
        )

        web_links = WebLinkService()

        for style in font["styles"]:
            web_links.add_new(
                style["file_name"],
                font["id"],
                style["style"],
                style["type"],
                consumer.get_cdn_link(
                    font["style_path"] + "/" + style["file_name"]
                )
            )

    def update_gitlab_font(self):
        print("Support disabled until we launch Fontman server.")

    def update_language_data(self, font_id, value):
        language = self.__languages.find_by_value(value)

        # add language if it's not in the database
        if language.count() is 0:
            self.__languages.add_new(True, value)

            # add font languages details
            self.__font_languages.add_new(
                font_id,
                self.__languages.find_by_value(value).one().id
            )

        else:
            self.__font_languages.add_new(
                font_id,
                self.__languages.find_by_value(value).one().id
            )
