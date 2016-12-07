""" Font controller

Provides flask blueprint using Font service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/11/2016
"""

from flask import Blueprint, jsonify

from service import FontService, WebLinkService

font_blueprint = Blueprint('font_blueprint', __name__)


def get_json_list(font_list_object):
    font_list = []
    status_color = "#57acf5"
    web_links = WebLinkService()

    for font_object in font_list_object:
        web_link = web_links.find_by_style(
            font_object.font_id,
            font_object.regular_style
        ).one().web_link

        # set font status color
        if font_object.installed and font_object.upgradable:
            status_color = "#fdbc40"
        elif font_object.installed:
            status_color = "#34c84a"

        font_list.append({
            "font_id": font_object.font_id,
            "installed": font_object.installed,
            "name": font_object.name,
            "sample": font_object.sample,
            "status_color": status_color,
            "upgradable": font_object.upgradable,
            "version": font_object.version,
            "web_link": web_link,
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


@font_blueprint.route('/font/web_link/<font_id>')
def get_web_links(font_id):
    json_list = []

    for link in WebLinkService().find_all_by_font_id(font_id):
        json_list.append(
            {
                "font_id": link.font_id,
                "file_name": link.file_name,
                "style": link.style,
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
