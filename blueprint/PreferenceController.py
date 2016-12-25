""" Preferences controller

Provides flask blueprint to manipulate fms settings.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 8/12/2016
"""

from flask import Blueprint, jsonify
from flask import request

from service import LanguageService
from service import SystemService

preference_blueprint = Blueprint('preference_blueprint', __name__)


@preference_blueprint.route("/preferences/languages/all")
def find_all():
    languages_list = []

    for language in LanguageService().find_all():
        languages_list.append(
            {
                "id": language.id,
                "is_enabled": language.is_enabled,
                "value": language.value
            }
        )

    return jsonify(languages_list)


@preference_blueprint.route("/preferences/refresh_rate")
def find_refresh_rate():
    return jsonify(SystemService().find_system_info().refresh_rate)


@preference_blueprint.route("/preferences/languages", methods=['POST'])
def update_languages():
    languages = LanguageService()
    new_languages_list = request.json

    for language in new_languages_list:
        languages.update_by_id(
            language["id"],
            {
                "is_enabled": language["is_enabled"]
            }
        )

    return jsonify(True)


@preference_blueprint.route("/preferences/refresh_rate/<value>")
def update_refresh_rate(value):
    SystemService().update_data({"refresh_rate": value})
    return jsonify(True)
