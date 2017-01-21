""" Cache Manager

This module covers initializing system, install update fonts, database
manipulation like operations.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from consumer import FontFacesConsumer
from consumer import FontsConsumer
from consumer import ChannelsConsumer
from service import ChannelService
from service import FontFaceService
from service import FontService
from service import InstalledFontService


class CacheManager:

    def find_changes(self, local_tb_ids, remote_tb_ids):
        new_list = []
        removal_list = []
        update_list = []

        for id in local_tb_ids:
            if remote_tb_ids:
                update_list.append(id)
            else:
                removal_list.append(id)

        for id in update_list:
            if id not in remote_tb_ids:
                new_list.append(id)

        return new_list, removal_list, update_list

    def add_new_channel(self, channel_id):
        new_channel = ChannelsConsumer().consume_by_channel_id(channel_id)

        ChannelService().add_new(
            new_channel["channel_id"],
            new_channel["name"],
            new_channel["type"]
        )

    def add_new_fontfaces(self, new_fontfaces):
        for fontface in new_fontfaces:
            FontFaceService().add_new(
                fontface["fontface_id"],
                fontface["download_url"],
                fontface["font_id"],
                fontface["fontface"],
                fontface["resource_path"]
            )

    def add_new_font(self, font_id):
        new_font = FontsConsumer().consume_by_font_id(font_id)
        new_fontfaces = FontFacesConsumer().consume_by_query(font_id)

        FontService().add_new(
            new_font["font_id"],
            new_font["channel_id"],
            new_font["name"],
            new_font["type"]
        )
        self.add_new_fontfaces(new_fontfaces)

    def gather_font_updates(self):
        font_ids = FontService().find_all_font_ids()

        for font_id in font_ids:
            font_data = FontService().find_by_font_id(font_id).first()

            if font_data.is_installed:
                latest_rel_data = FontsConsumer().consume_latest_rel_info(
                    font_id
                )
                if latest_rel_data["tag_name"] not in InstalledFontService(
                ).find_by_font_id(font_id).first()["version"]:
                    FontService().update_by_font_id(
                        font_id,
                        {
                            "is_upgradable": True
                        }
                    )

    def update_channels_cache(self):
        local_id_list = ChannelService().find_all_channel_ids()
        remote_id_list = ChannelsConsumer().consume_all_channels()

        if local_id_list.first() is None and remote_id_list is not []:
            for channel_id in remote_id_list:
                self.add_new_channel(channel_id)

        elif local_id_list.first() is not None and remote_id_list is not []:
            new_list, removal_list, update_list = self.find_changes(
                local_id_list, remote_id_list
            )

            if new_list is not []:
                for channel_id in new_list:
                    self.add_new_channel(channel_id)

            if update_list is not []:
                for channel_id in update_list:
                    channel_data = ChannelsConsumer().consume_by_channel_id(
                        channel_id
                    )

                    ChannelService().update_by_channel_id(
                        channel_id,
                        {
                            "name": channel_data["name"],
                            "type": channel_data["type"]
                        }
                    )

    def update_fonts_cache(self):
        local_id_list = FontService().find_all_font_ids()
        remote_id_list = FontsConsumer().consume_all_fonts()

        if local_id_list.first() is None and remote_id_list is not []:
            for font_id in remote_id_list:
                self.add_new_font(font_id)

        elif local_id_list.first() is not None and remote_id_list is not []:
            new_list, removal_list, update_list = self.find_changes(
                local_id_list, remote_id_list
            )

            if new_list is not []:
                for font_id in new_list:
                    self.add_new_font(font_id)

            if update_list is not []:
                for font_id in update_list:
                    font_data = FontsConsumer().consume_by_font_id(font_id)
                    FontService().update_by_font_id(
                        font_id,
                        {
                            "name": font_data["name"],
                            "type": font_data["type"]
                        }
                    )

                    FontFaceService().delete_by_font_id(font_id)
                    self.add_new_fontfaces(
                        FontFacesConsumer().consume_by_query(font_id)
                    )
