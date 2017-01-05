""" Fontman server teams consumer

Consume and sync with fontman server teams REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class TeamsConsumer:

    def consume_all_teams(self):
        response = requests.get(api_base_url + '/teams')
        return json.loads(response.text)

    def consume_by_team_id(self, team_id):
        response = requests.get(api_base_url + '/teams/' + team_id)
        return json.loads(response.text)

    def consume_by_query(self, type):
        response = requests.get(
            api_base_url + '/teams?type=' + type
        )
        return json.loads(response.text)

    def consume_new_team(self, json_data):
        response = requests.post(
            api_base_url + '/teams/new', json=json_data
        )
        return json.loads(response.text)

    def consume_delete_team(self, team_id, json_data):
        response = requests.post(
            api_base_url + '/teams/' + team_id + '/delete',
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_team(self, team_id, json_data):
        response = requests.post(
            api_base_url + '/teams/' + team_id + '/update',
            json=json_data
        )
        return json.loads(response.text)
