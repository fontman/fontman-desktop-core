""" Font-faces controller

REST blueprint to obtain font-faces information.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/1/2017
"""

from service import FontFaceService

from flask import Blueprint, jsonify, request

fontfaces_blueprint = Blueprint("fontfaces_blueprint", __name__)


@fontfaces_blueprint.route("/fontfaces")
def find_all_fontfaces():
    response_data = []

    for fontface in FontFaceService().find_all():
        response_data.append(
            {
                "fontface_id": fontface.fontface_id,
                "fontface": fontface.fontface,
                "font_id": fontface.font_id,
                "resource_path": fontface.resource_path
            }
        )

    return jsonify(response_data)


@fontfaces_blueprint.route("/fontfaces/<fontface_id>")
def find_fontface_by_fontface_id(fontface_id):
    try:
        fontface = FontFaceService().find_by_fontface_id(fontface_id).one()
        return jsonify(
            {
                "fontface_id": fontface.fontface_id,
                "fontface": fontface.fontface,
                "font_id": fontface.font_id,
                "resource_path": fontface.resource_path
            }
        )

    except:
        return jsonify({"error": "Font face does not exists"})


@fontfaces_blueprint.route("/fontfaces/")
def find_fontface_by_font_id():
    response_data = []

    try:
        query_string = request.args.get("font_id")
        fontfaces = FontFaceService().find_by_font_id(query_string)

        for fontface in fontfaces:
            response_data.append(
                {
                    "fontface_id": fontface.fontface_id,
                    "fontface": fontface.fontface,
                    "font_id": fontface.font_id,
                    "resource_path": fontface.resource_path
                }
            )

        return jsonify(response_data)

    except:
        return jsonify({"error": "Invalid request"})
