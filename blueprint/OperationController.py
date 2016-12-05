""" Operation controller

Provides flask blueprint to manage font installations, removal, updates and
repository cache.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify, request

from utility import Operation

operation_blueprint = Blueprint('operation_blueprint', __name__)


@operation_blueprint.route('/operation/install/<font_id>')
def install_font(font_id):
    return jsonify(Operation().install_font(font_id))


@operation_blueprint.route('/operation/remove/<font_id>')
def remove_font(font_id):
    return jsonify(Operation().remove_font(font_id))


@operation_blueprint.route('/operation/update/<font_id>')
def update_font(font_id):
    return jsonify(Operation().update_font(font_id))
