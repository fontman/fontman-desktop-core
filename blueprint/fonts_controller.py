""" Fonts controller

Provides fonts REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import FontsConsumer
from service import FontFaceService
from service import FontService
from service import MetadataService
from service import RoleService
from service import ProfileService

fonts_blueprint = Blueprint("fonts_blueprint", __name__)


@fonts_blueprint.route("/fonts")
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        response_data.append(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "is_installed": font.is_installed,
                "name": font.name,
                "type": font.type,
                "is_upgradable": font.is_upgradable
            }
        )

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/admin")
def find_all_user_fonts():
    response_data = []
    font_privileges = RoleService().find_by_entity("font")

    for privilege in font_privileges:
        if privilege.role in "admin":
            font = FontService().find_by_font_id(privilege.entity_id).first()

            response_data.append(
                {
                    "font_id": font.font_id,
                    "name": font.name,
                    "type": font.type
                }
            )

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/<font_id>")
def find_by_font_id(font_id):
    font = FontService().find_by_font_id(font_id)
    return jsonify(
        {
            "font_id": font.font_id,
            "channel_id": font.channel_id,
            "is_installed": font.is_installed,
            "name": font.name,
            "type": font.type,
            "is_upgradable": font.is_upgradable
        }
    )


@fonts_blueprint.route("/fonts/<font_id>/metadata")
def find_metadata_by_font_id(font_id):
    metadata = MetadataService().find_by_font_id(font_id).first()

    return jsonify(
        {
            "metadata_id": metadata.metadata_id,
            "font_id": metadata.font_id,
            "latest_tag_url": metadata.latest_tag_url,
            "tags_url": metadata.tags_url
        }
    )


@fonts_blueprint.route("/fonts/new", methods=["POST"])
def add_new_font():
    json_data = request.json
    profile = ProfileService().find_user()

    json_data["user_id"] = profile.user_id
    json_data["token"] = profile.token

    response = FontsConsumer().consume_new_font(json_data)

    if "error" in response:
        return jsonify(response)

    else:
        FontService().add_new(
            response["font_id"],
            response["channel_id"],
            response["name"],
            response["type"]
        )
        tags_info = FontsConsumer().consume_tags_url(response["font_id"])

        MetadataService().add_new(
            tags_info["font_id"],
            "https://api.github.com/repos/" + json_data["gitUser"] + "/"
            + json_data["gitRepository"] + "/releases/latest",
            tags_info["tags_url"]
        )

        for fontface in response["fontfaces"]:
            FontFaceService().add_new(
                response["font_id"],
                fontface["fontface"],
                fontface["fontface_id"],
                fontface["resource_path"]
            )

        RoleService().add_new(
            response["role_id"],
            response["font_id"],
            "font",
            "admin"
        )

        return jsonify(True)
