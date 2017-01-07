""" Teams controller

Provides teams REST API for Fontman client GUI

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 7/1/2017
"""

from flask import Blueprint, jsonify, request

from consumer import TeamsConsumer
from service import ProfileService
from service import RoleService
from service import TeamService

teams_blueprint = Blueprint('teams_blueprint', __name__)


@teams_blueprint.route('/teams/new', methods=['POST'])
def add_new_team():
    json_data = request.data
    profile = ProfileService().find_user()

    json_data["user_id"] = profile.user_id
    json_data["token"] = profile.token

    response = TeamsConsumer().consume_new_team(json_data)

    if "error" in response:
        return jsonify(response)

    else:
        RoleService().add_new(
            response["role_id"],
            "team",
            response["team_id"],
            "admin"
        )

        TeamService().add_new(
            response["team_id"],
            response["name"],
            response["type"]
        )

        return jsonify(True)


@teams_blueprint.route('/teams/<team_id>')
def find_team_by_team_id(team_id):
    team = TeamService().find_by_team_id(team_id).one()

    return jsonify(
        {
            "team_id": team.team_id,
            "name": team.name,
            "type": team.type
        }
    )


@teams_blueprint.route('/teams/<team_id>/update', methods=['POST'])
def update_team_data(team_id):
    json_data = request.data
    profile = ProfileService().find_user()

    json_data["user_id"] = profile.user_id
    json_data["token"] = profile.token

    response = TeamsConsumer().consume_update_team(team_id, json_data)

    if "error" in response:
        return jsonify(response)

    else:
        TeamService().update_by_team_id(team_id, response)
