""" Fonts controller

Provides fonts REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from service import FontFaceService
from service import FontService
from service import LanguageService
from service import MetadataService
from utility import FontManager

from flask import Blueprint, jsonify, request

fonts_blueprint = Blueprint("fonts_blueprint", __name__)


@fonts_blueprint.route("/fonts")
def find_all_fonts():
    response_data = []
    fonts = FontService().find_all()

    for font in fonts:
        metadata = MetadataService().find_by_font_id(font.font_id)
        fontfaces = FontFaceService().find_by_font_id(font.font_id)
        languages = LanguageService().find_by_font_id(font.font_id)

        fontfaces_list = []
        languages_list = []

        for fontface in fontfaces:
            fontfaces_list.append(
                {
                    "fontface": fontface.fontface,
                    "resource_path": fontface.resource_path
                }
            )

        for language in languages:
            languages_list.append(language.language)

        response_data.append(
            {
                "font_id": font.font_id,
                "chosen": font.is_chosen,
                "default_fontface": metadata.default_fontface,
                "displayText": font.name,
                "fontfaces": fontfaces_list,
                "is_installed": font.is_installed,
                "is_upgradable": font.is_upgradable,
                "name": font.name
            }
        )

    return jsonify(response_data)


@fonts_blueprint.route("/fonts/status/chosen")
def find_chosen_fonts_status():
    if FontService().find_all_chosen().first() is None:
        return jsonify(False)
    else:
        return jsonify(True)


@fonts_blueprint.route("/fonts/<font_id>/install")
def install_font_by_font_id(font_id):
    response = FontManager().install_font(font_id)
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

                for fontface in fontfaces:
                    if "regular" in fontface.fontface.lower():
                        regular_fontface = fontface.fontface

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
                        "selectedFontface": regular_fontface,
                        "type": font.type,
                        "is_upgradable": font.is_upgradable
                    }
                )

            return jsonify(response_data)

    except:
        return jsonify({"error": "Invalid request"})


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
