""" Settings controller

Provides settings REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak <lpsandaruwan@gmail.com> on 5/2/2017
"""

from datetime import date
from flask import Blueprint, jsonify, request

from service import SystemService

settings_blueprint = Blueprint("settings_blueprint", __name__)


@settings_blueprint.route("/settings/about")
def find_app_info():
    system = SystemService().find_system_info()
    return jsonify(
        {
            "platform": system.platform,
            "version": system.version,
            "year": date.today().year
        }
    )