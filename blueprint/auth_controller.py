""" Authentication controller

Handling authentication and user management between FMS and Fontman GUI.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import AuthConsumer
from consumer import UsersConsumer
from service import ProfileService

auth_blueprint = Blueprint("auth_blueprint", __name__)


@auth_blueprint.route("/auth/login", methods=["POST"])
def login():
    request_data = request.json
    profile_data = ProfileService().find_by_email(request_data["email"])

    json_data = {
        "email": request_data["email"],
        "password": request_data["password"]
    }

    auth_response = AuthConsumer().consume_login(json_data)

    if "error" in auth_response:
        return jsonify(auth_response)

    if profile_data is None:
        user_data = UsersConsumer().consume_by_user_id(auth_response["user_id"])

        ProfileService().add_new(
            user_data["user_id"],
            request_data["email"],
            user_data["name"],
            request_data["passsword"],
            auth_response["token"]
        )

    else:
        ProfileService().update_by_user_id(
            auth_response["user_id"],
            {
                "is_logged": True,
                "token": auth_response["token"]
            }
        )

    return jsonify(True)


@auth_blueprint.route("/auth/<user_id>/logout")
def logout(user_id):
    ProfileService().set_active_mode(user_id, False)
    return jsonify(True)


@auth_blueprint.route("/auth/profile")
def profile_info():
    profile = ProfileService().find_logged_user()

    return jsonify(
        {
            "user_id": profile.user_id,
            "name": profile.name,
        }
    )


@auth_blueprint.route("/auth/new/profile", methods=["POST"])
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


@auth_blueprint.route("/auth/status")
def find_status():
    if ProfileService().find_all().first() is None:
        return jsonify({"status": "undefined"})

    else:
        if ProfileService().find_logged_user() is None:
            return jsonify({"status": False})

        else:
            return jsonify({"status": True})
