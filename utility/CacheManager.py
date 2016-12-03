""" Cache Manager

This module covers initializing system, install update fonts, database
manipulation like operations.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import requests

from consumer import GitHubConsumer
from service import ChannelService, FontService, GithubFontService


class CacheManager:

    def __init__(self):
        self.__channel_service = ChannelService()
        self.__font_service = FontService()
        self.__github_font_service = GithubFontService()

    def update_github_font_cache(self):
        channels = self.__channel_service.find_by_channel_type("github")

        for channel in channels:
            # get fonts list from channel
            fonts_list = requests.get(channel.base_url).json()

            # update fonts information
            for font in fonts_list:
                # get font data using github API
                latest_release = GitHubConsumer(
                    font["branch"], font["repository"], font["user"]
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

                    continue

                # add a record in fonts directory
                self.__font_service.add_new(
                    font["id"],
                    channel.channel_id,
                    release_info["name"],
                    font["name"],
                    release_info["browser_download_url"],
                    latest_release["tag_name"]
                )

                # add a detailed infromation record in github fonts table
                self.__github_font_service.add_new(
                    font["id"],
                    font["branch"],
                    font["path"],
                    font["repository"],
                    font["user"]
                )
