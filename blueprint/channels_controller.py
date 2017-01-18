""" Channels controller

REST blueprint to provide channel API

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/1/2017
"""

from flask import Blueprint, jsonify

from service import ChannelService

channels_blueprint = Blueprint("channels_blueprint", __name__)


@channels_blueprint.route("/channels")
def find_all_channels():
    response = []

    for channel in ChannelService().find_all():
        response.append(
            {
                "channel_id": channel.channel_id,
                "is_active": channel.is_active,
                "name": channel.name,
                "type": channel.type
            }
        )

    return jsonify(response)
