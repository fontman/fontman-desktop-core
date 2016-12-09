""" Channel controller

Flask services to manipulate channels

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/12/2016
"""

from flask import Blueprint, jsonify, request

from service import ChannelService

channel_blueprint = Blueprint('channel_blueprint', __name__)


@channel_blueprint.route("/channels/all")
def find_all():
    channels = ChannelService().find_all()
    channels_list = []

    for channel in channels:
        channels_list.append(
            {
                "channel_id": channel.channel_id,
                "base_url": channel.base_url,
                "is_active": channel.is_active,
                "license_key": channel.license_key,
                "type": channel.type
            }
        )

        return jsonify(channels_list)


@channel_blueprint.route("/channel/save", methods=['POST'])
def save_channel():
    new_channel = request.json

    ChannelService.add_new(
        new_channel["channel_id"],
        new_channel["base_url"],
        new_channel["type"],
        new_channel["license_key"]
    )

    return jsonify(True)


