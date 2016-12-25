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
            "secret": profile_data["secret"]
        }
    )

    ProfileService().add_new(
        validated_data["user_id"],
        validated_data["email"],
        True,
        validated_data["name"],
        validated_data["key"]
    )

    return jsonify(True)


@profile_blueprint.route('/profile/status')
def status_check():
    user = ProfileService().find_user()

    if user is None:
        return jsonify(False)
    else:
        return jsonify(
            {
                "email": user.email,
                "name": user.name,
                "key": user.key
            }
        )
