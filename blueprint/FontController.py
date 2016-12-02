""" Font controller

Provides flask blueprints using Font service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify, request

font_blueprint = Blueprint('font_blueprint', __name__)
font_service = Font()


@font_blueprint.route('/font/all', methods=['GET'])
def find_all():
    return jsonify(font_service.find_all())


@font_blueprint.route('/font/check/install/<font_id>')
def is_installable(font_id):
    return jsonify(font_service.is_installed(font_id))


@font_blueprint.route('/font/check/update/<font_id>')
def is_upgradable(font_id):
    return jsonify(font_service.is_upgradable(font_id))
