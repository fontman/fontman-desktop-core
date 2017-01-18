""" Fontman server auth services consumer

Consume and sync with fontman server authentication REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class AuthConsumer:

    def consume_login(self, json_data):
        response = requests.post(api_base_url + "/auth/login", json=json_data)
        return json.loads(response.text)

    def consume_new_user(self, json_data):
        response = requests.post(
            api_base_url + "/auth/new/user",
            json=json_data
        )
        return json.loads(response.text)

    def consume_new_password(self, json_data):
        response = requests.post(
            api_base_url + "/auth/new/password",
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_token(self, json_data):
        response = requests.post(
            api_base_url + "/auth/update/token",
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_user(self, json_data):
        response = requests.post(
            api_base_url + "/auth/update/user",
            json=json_data
        )
        return json.loads(response.text)
