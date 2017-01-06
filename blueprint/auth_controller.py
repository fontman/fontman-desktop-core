""" Authentication controller

Handling authentication and user management between FMS and Fontman GUI.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import AuthConsumer
from service import ProfileService

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route('/auth/login', methods=['POST'])
def login():
    request_data = request.json
    profile_data = ProfileService().find_user()

    if request_data["email"] in profile_data.email and request_data["password"]\
            in profile_data.password:
        json_data = {
            "email": request_data["email"],
            "password": request_data["password"]
        }
        response = AuthConsumer().consume_login(json_data)

        if "error" in response:
            return jsonify(response)

        if response in ProfileService().find_user().token:
            ProfileService().set_active_mode(True)
            return jsonify(True)

        else:
            return jsonify({"error": "Token mismatch, contact admin"})

    else:
        return jsonify({"error": "Invalid email or password"})


@auth_blueprint.route('/auth/new/profile', methods=['POST'])
def add_new_profile():
    request_data = request.json
    response = AuthConsumer().consume_new_user(request_data)

    if "error" in response:
        return jsonify(response)

    else:
        ProfileService().add_new(
            response["user_id"],
            response["email"],
            response["name"],
            response["password"],
            response["token"],
        )

        return jsonify(True)
