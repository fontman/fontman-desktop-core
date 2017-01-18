""" Fontman server users consumer

Consume and sync with fontman server users REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class UsersConsumer:

    def consume_all_users(self):
        response = requests.get(api_base_url + "/users")
        return json.loads(response.text)

    def consume_by_user_id(self, user_id):
        response = requests.get(api_base_url + "/users/" + user_id)
        return json.loads(response.text)
