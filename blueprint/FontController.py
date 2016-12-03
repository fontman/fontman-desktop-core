""" Font controller

Provides flask blueprints using Font service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify, request

from service import FontIndexService, FontService

font_blueprint = Blueprint('font_blueprint', __name__)
font_service = FontService()
font_index_service = FontIndexService()


@font_blueprint.route('/font/all', methods=['GET'])
def find_all():
    font_list = []

    for font in font_service.find_all():
        font_list.append({
            "font_id": font.font_id,
            "name": font.name,
            "version": font.version
        })

    return jsonify(font_list)


@font_blueprint.route('/font/check/installed/<font_id>')
def is_installable(font_id):
    return jsonify(font_index_service.find_by_font_id(font_id).installed)


@font_blueprint.route('/font/check/upgradable/<font_id>')
def is_upgradable(font_id):
    return jsonify(font_index_service.find_by_font_id(font_id).upgradable)
