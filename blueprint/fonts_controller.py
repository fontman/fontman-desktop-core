""" Fonts controller

Provides fonts REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

import time
from flask import Blueprint, jsonify, request

from consumer import FontsConsumer
from service import FontFaceService
from service import FontService
from service import MetadataService
from service import RoleService
from service import ProfileService
from utility import FontManager

fonts_blueprint = Blueprint("fonts_blueprint", __name__)


@fonts_blueprint.route("/fonts")
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        if font.is_chosen:
            continue

        fontfaces = FontFaceService().find_by_font_id(font.font_id)
        fontfaces_list = []
        regular_fontface = None
        regular_font_url = None

        for fontface in fontfaces:
            if "regular" in fontface.fontface.lower():
                regular_fontface = fontface.fontface
                regular_font_url = fontface.resource_path

            fontfaces_list.append(
                {
                    "fontface": fontface.fontface,
                    "resource_path": fontface.resource_path
                }
            )

        response_data.append(
            {
                "font_id": font.font_id,
                "channel_id": font.channel_id,
                "chosen": font.is_chosen,
                "displayText": font.name,
                "fontfaces": fontfaces_list,
                "is_installed": font.is_installed,
                "name": font.name,
                "regularFontUrl": regular_font_url,
                "selectedFontface": regular_fontface,
                "type": font.type,
                "is_upgradable": font.is_upgradable
            }
        )

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/status/chosen")
def find_chosen_fonts_status():
    if FontService().find_all_chosen().first() is None:
        return jsonify(False)
    else:
        return jsonify(True)


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
    font = FontService().find_by_font_id(font_id).first()
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


@fonts_blueprint.route("/fonts/<font_id>/releases")
def find_tags_by_font_id(font_id):
    response = [{"id": "devel", "tag_name": "devel"}]
    rel_info = FontsConsumer().consume_releases(font_id)

    for release in rel_info:
        response.append(
            {
                "id": release["id"],
                "tag_name": release["tag_name"]
            }
        )

    return jsonify(response)


@fonts_blueprint.route("/fonts/<font_id>/install/<rel_id>")
def install_font_by_font_id(font_id, rel_id):
    response = FontManager().install_font(font_id, rel_id)
    return jsonify(response)


@fonts_blueprint.route("/fonts/<font_id>/reinstall/<rel_id>")
def reinstall_font_by_font_id(font_id, rel_id):
    response = False

    if FontManager().remove_font(font_id):
        time.sleep(0.5)
        response = FontManager().install_font(font_id, rel_id)

    return jsonify(response)


@fonts_blueprint.route("/fonts/")
def find_by_query():
    response_data = []

    try:
        if request.args.get("is_chosen"):
            chosen_fonts = FontService().find_all_chosen()

            for font in chosen_fonts:
                fontfaces = FontFaceService().find_by_font_id(font.font_id)
                fontfaces_list = []
                regular_fontface = None
                regular_font_url = None

                for fontface in fontfaces:
                    if "regular" in fontface.fontface.lower():
                        regular_fontface = fontface.fontface
                        regular_font_url = fontface.resource_path

                    fontfaces_list.append(
                        {
                            "fontface": fontface.fontface,
                            "resource_path": fontface.resource_path
                        }
                    )

                response_data.append(
                    {
                        "font_id": font.font_id,
                        "channel_id": font.channel_id,
                        "chosen": font.is_chosen,
                        "displayText": font.name,
                        "fontfaces": fontfaces_list,
                        "is_installed": font.is_installed,
                        "name": font.name,
                        "regularFontUrl": regular_font_url,
                        "selectedFontface": regular_fontface,
                        "type": font.type,
                        "is_upgradable": font.is_upgradable
                    }
                )

            return jsonify(response_data)

    except:
        return jsonify({"error": "Invalid request"})


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
    profile = ProfileService().find_logged_user()

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
        tags_info = FontsConsumer().consume_metadata_by_font_id(
            response["font_id"]
        )

        MetadataService().add_new(
            tags_info["font_id"],
            "https://api.github.com/repos/"
            + json_data["gitUser"] + "/"
            + json_data["gitRepository"] + "/releases/latest",
            tags_info["tags_url"]
        )

        for fontface in response["fontfaces"]:
            FontFaceService().add_new(
                fontface["fontface_id"],
                fontface["download_url"],
                response["font_id"],
                fontface["fontface"],
                fontface["resource_path"]
            )

        RoleService().add_new(
            response["role_id"],
            response["font_id"],
            "font",
            "admin"
        )

        return jsonify(True)


@fonts_blueprint.route("/fonts/update", methods=["POST"])
def update_all_fonts():
    json_data = request.json
    FontService().update_all(json_data)

    return jsonify(json_data)


@fonts_blueprint.route("/fonts/<font_id>/update", methods=["POST"])
def update_font_by_font_id(font_id):
    json_data = request.json
    FontService().update_by_font_id(font_id, json_data)

    return jsonify(True)
