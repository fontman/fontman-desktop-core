""" About controller

Flask services to get fontman/platform details

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/12/2016
"""

from flask import Blueprint, jsonify

from service import SystemService

about_blueprint = Blueprint('about_blueprint', __name__)


@about_blueprint.route("/about")
def about():
    system_info = SystemService().find_system_info()

    return jsonify(
        {
            "platform": system_info.platform,
            "user": system_info.system_user,
            "version": system_info.version
        }
    )
