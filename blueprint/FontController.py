""" Font controller

Provides flask blueprint using Font service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify
from flask import request

from consumer import FontmanConsumer
from service import ChannelService
from service import FontLanguageService
from service import FontService
from service import LanguageService

font_blueprint = Blueprint('font_blueprint', __name__)


def get_json_list(font_list_object):
    channels = ChannelService()
    enabled_languages_id_list = []
    font_id_list = []
    font_languages = FontLanguageService()
    font_list = []

    # collect enabled languages ids
    for language in LanguageService().find_all_enabled():
        enabled_languages_id_list.append(language.id)

    # collect font ids to display
    for language_id in enabled_languages_id_list:
        for element in font_languages.find_by_language_id(language_id):
            if element.font_id in font_id_list:
                continue
            font_id_list.append(element.font_id)

    for font_object in font_list_object:
        # skip font if channel is disabled
        if not channels.find_enabled_by_channel_id(font_object.channel_id):
            continue

        # skip font if it is disabled by languages
        if font_object.font_id not in font_id_list:
            continue

        # set font status color
        status_color = "#57acf5"

        if font_object.installed:
            status_color = "#34c84a"

        if font_object.upgradable:
            status_color = "#fdbc40"

        font_list.append({
            "font_id": font_object.font_id,
            "installed": font_object.installed,
            "name": font_object.name,
            "preview_cdn": font_object.preview_cdn,
            "sample": font_object.sample,
            "status_color": status_color,
            "type": font_object.type,
            "upgradable": font_object.upgradable,
            "version": font_object.version,
        })

    return font_list


@font_blueprint.route('/font/add', methods=['POST'])
def add_new_font():
    font_data = request.json
    new_font = {
        font_data["font_id"],
        font_data["channel_id"],
        font_data["name"],
        font_data["preview_cdn"],
        font_data["sample"],
        font_data["type"],
        font_data["url"],
        font_data["version"]
    }

    server_data = FontmanConsumer().consume_new_font(new_font)
    FontService().add_new(
        server_data["font_id"],
        server_data["channel_id"],
        server_data["name"],
        server_data["preview_cdn"],
        server_data["sample"],
        server_data["type"],
        server_data["url"],
        server_data["version"]
    )

    return jsonify(True)


@font_blueprint.route('/font/all', methods=['GET'])
def find_all():
    return jsonify(get_json_list(FontService().find_all()))


@font_blueprint.route('/font/one/<font_id>')
def find_one(font_id):
    return jsonify(get_json_list(FontService().find_by_font_id(font_id))[0])


@font_blueprint.route('/font/installable')
def get_all_installable():
    return get_json_list(FontService().find_all_installable())


@font_blueprint.route('/font/installed')
def get_all_installed():
    return get_json_list(FontService().find_all_installed())


@font_blueprint.route('/font/upgradable')
def get_all_upgradable():
    return get_json_list(FontService().find_all_upgradable())


@font_blueprint.route('/font/check/installed/<font_id>')
def is_installed(font_id):
    return jsonify(FontService().find_by_font_id(font_id).one().installed)


@font_blueprint.route('/font/upgrade', methods=['POST'])
def update_font_by_id():
    font_data = request.json
    server_data = FontmanConsumer().consume_update_font(font_data)
    font = FontService().find_by_font_id(server_data["font_id"])

    if font.installed:
        if font.version not in server_data["version"]:
            FontService().update_by_font_id(
                server_data["font_id"],
                {
                    "upgradable": True,
                    "url": server_data["url"],
                    "version": server_data["version"]
                }
            )
    else:
        FontService().update_by_font_id(
            server_data["font_id"],
            {
                "url": server_data["url"],
                "version": server_data["version"]
            }
        )

    return jsonify(True)


@font_blueprint.route('/font/check/upgradable/<font_id>')
def is_upgradable(font_id):
    return jsonify(FontService().find_by_font_id(font_id).one().upgradable)
