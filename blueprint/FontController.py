""" Font controller

Provides flask blueprint using Font service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify, request

from service import FontService, GithubFontService, WebLinkService

font_blueprint = Blueprint('font_blueprint', __name__)


def get_json_list(font_list_object):
    font_list = []

    for font_object in font_list_object:
        font_list.append({
            "font_id": font_object.font_id,
            "name": font_object.name,
            "version": font_object.version
        })

    return jsonify(font_list)


@font_blueprint.route('/font/all', methods=['GET'])
def find_all():
    return get_json_list(FontService().find_all())


@font_blueprint.route('/font/installable')
def get_all_installable():
    return get_json_list(FontService().find_all_installable())


@font_blueprint.route('/font/installed')
def get_all_installed():
    return get_json_list(FontService().find_all_installed())


@font_blueprint.route('/font/upgradable')
def get_all_upgradable():
    return get_json_list(FontService().find_all_upgradable())


@font_blueprint.route('/font/sample/<font_id>')
def get_sample_text(font_id):
    sample_text = GithubFontService().find_by_font_id(font_id).one().sample

    return jsonify(
        {
            "font_id": font_id,
            "sample": sample_text
        }
    )


@font_blueprint.route('/font/web_link/<font_id>')
def get_web_links(font_id):
    json_list = []

    for link in WebLinkService().find_all_by_font_id(font_id):
        json_list.append(
            {
                "font_id": link.font_id,
                "file_name": link.file_name,
                "web_link": link.web_link
            }
        )
    return jsonify(json_list)


@font_blueprint.route('/font/check/installed/<font_id>')
def is_installed(font_id):
    return jsonify(FontService().find_by_font_id(font_id).one().installed)


@font_blueprint.route('/font/check/upgradable/<font_id>')
def is_upgradable(font_id):
    return jsonify(FontService().find_by_font_id(font_id).one().upgradable)
