""" Channel controller

Flask services to manipulate channels

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/12/2016
"""

from flask import Blueprint, jsonify
from flask import request

from consumer import FontmanConsumer
from service import ChannelService

channel_blueprint = Blueprint('channel_blueprint', __name__)


@channel_blueprint.route("/channel/add", methods=['POST'])
def add_new_channel():
    new_channel = request.json
    validated_channel = FontmanConsumer().consume_new_channel(
        {
            "key": new_channel["key"],
            "name": new_channel["name"],
            "type": new_channel["type"]
        }
    )

    ChannelService().add_new(
        validated_channel["channel_id"],
        validated_channel["key"],
        validated_channel["name"],
        validated_channel["type"]
    )

    return jsonify(True)


@channel_blueprint.route("/channel/status", methods=["POST"])
def change_channel_status():
    channel_data = request.json
    ChannelService().update_by_channel_id(
        channel_data["channel_id"],
        {"is_active": channel_data["is_active"]}
    )

    return jsonify(True)


@channel_blueprint.route("/channel/all")
def find_all():
    channels = ChannelService().find_all()
    channels_list = []

    for channel in channels:
        channels_list.append(
            {
                "channel_id": channel.channel_id,
                "is_active": channel.is_active,
                "key": channel.key,
                "type": channel.type
            }
        )

    return jsonify(channels_list)


@channel_blueprint.route("/channel/info/<channel_id>")
def find_by_id(channel_id):
    channel_data = ChannelService().find_by_channel_id(channel_id).one()

    return jsonify(
        {
            "channel_id": channel_data.channel_id,
            "base_url": channel_data.base_url,
            "is_active": channel_data.is_active,
            "type": channel_data.type
        }
    )


@channel_blueprint.route("/channel/refresh/<channel_id>")
def refresh_by_channel_id(channel_id):
    return jsonify(True)


@channel_blueprint.route("/channel/remove/<channel_id>")
def delete_by_channel_id(channel_id):
    ChannelService().delete_by_channel_id(channel_id)

    return jsonify(True)

