""" Auth controller

Flask services to handle authentications

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/12/2016
"""

from flask import Blueprint, jsonify
from flask import request

from consumer import FontmanConsumer
from service import ProfileService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/auth/status')
def is_logged_in():
    user = ProfileService().find_user()

    if user is None:
        return jsonify({"status": "no_user"})

    else:
        if user.is_active:
            return jsonify(
                {
                    "status": True,
                    "uuid": user.uuid
                }
            )

        else:
            return jsonify({"status": False})


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    auth_data = request.json
    response_json = FontmanConsumer().login(
        {
            "username": auth_data["username"],
            "password": auth_data["password"]
        }
    )

    if "unauthorized" in response_json:
        return jsonify(False)
    else:
        ProfileService().update_user(
            {"is_active": True, "uuid": response_json}
        )

        return jsonify(True)


@auth_blueprint.route('/auth/logout')
def logout():
    ProfileService().update_user({"is_active": False})
    return jsonify(True)
