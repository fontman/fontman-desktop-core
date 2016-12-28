""" Profile controller

User login and details controller.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/12/2016
"""
from flask import Blueprint, jsonify
from flask import request

from consumer import FontmanConsumer
from service import ProfileService

profile_blueprint = Blueprint('profile_blueprint', __name__)


@profile_blueprint.route('/profile/add', methods=['POST'])
def add_user():
    profile_data = request.json
    validated_data = FontmanConsumer().consume_new_user(
        {
            "email": profile_data["email"],
            "name": profile_data["name"],
            "password": profile_data["password"],
            "username": profile_data["username"]
        }
    )

    ProfileService().add_new(
        validated_data["user_id"],
        validated_data["email"],
        validated_data["name"],
        validated_data["password"],
        validated_data["username"],
        validated_data["uuid"]
    )

    return jsonify(True)
