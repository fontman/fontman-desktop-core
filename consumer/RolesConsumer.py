""" Fontman server roles consumer

Consume and sync with fontman server roles REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class RolesConsumer:

    def consume_by_entity_id(self, entity, entity_id, user_id):
        response = requests.get(
            api_base_url + '/roles/' + entity + '/' + entity_id + '?user_id='
            + user_id
        )
        return json.loads(response.text)

    def consume_new_role(self, json_data):
        response = requests.post(
            api_base_url + '/roles/new', json=json_data
        )
        return json.loads(response.text)

    def consume_delete_role(self, role_id, json_data):
        response = requests.post(
            api_base_url + '/roles/' + role_id + '/delete',
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_role(self, role_id, json_data):
        response = requests.post(
            api_base_url + '/roles/' + role_id + '/update',
            json=json_data
        )
        return json.loads(response.text)
