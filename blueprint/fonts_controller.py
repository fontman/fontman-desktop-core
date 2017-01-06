""" Fonts controller

Provides fonts REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import FontsConsumer
from service import FontFaceService
from service import FontService
from service import ProfileService

fonts_blueprint = Blueprint('fonts_blueprint', __name__)


@fonts_blueprint.route('/fonts')
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        response_data.append(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "installed": font.installed,
                "name": font.name,
                "team_id": font.team_id,
                "type": font.type,
                "upgradable": font.upgradable
            }
        )

    return jsonify(response_data)


@fonts_blueprint.route('/fonts/<font_id>')
def find_by_font_id(font_id):
    font = FontService().find_by_font_id(font_id)
    return jsonify(
        {
            "font_id": font.font_id,
            "channel_id": font.channel_id,
            "installed": font.installed,
            "name": font.name,
            "team_id": font.team_id,
            "type": font.type,
            "upgradable": font.upgradable
        }
    )


@fonts_blueprint.route('/fonts/new', methods=['POST'])
def add_new_font():
    request_data = request.json
    request_data["token"] = ProfileService().find_user().token

    response = FontsConsumer().consume_new_font(request_data)

    if "error" in response:
        return jsonify(response)

    else:
        FontService().add_new(
            response["font_id"],
            response["channel_id"],
            response["name"],
            response["team_id"],
            response["type"]
        )

        for fontface in response["fontfaces"]:
            FontFaceService().add_new_fontface(
                response["font_id"],
                fontface["fontface"],
                fontface["fontface_id"],
                fontface["resource_path"]
            )

        return jsonify(True)
