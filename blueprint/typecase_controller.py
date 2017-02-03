""" Typecase controller

Rest API to handle system fonts and curated/user collections.

Created by Lahiru Pathirage @ Mooniak <lpsandaruwan@gmail.com> on 2/2/2017
"""

from flask import Blueprint, jsonify

from utility import FontManager

typecase_blueprint = Blueprint("typecase_blueprint", __name__)


@typecase_blueprint.route("/system/fonts")
def get_active_fonts():
    return jsonify(FontManager().get_active_fonts_list())
