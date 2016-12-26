""" Fontman server consumer

Consume and sync with fontman server.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 22/12/2016
"""

from session import server

import json, requests


class FontmanConsumer:

    def consume_new_channel(self, json_data):
        response = requests.post(server + '/channel/add', json=json_data)
        return json.loads(response.text)

    def consume_new_font(self, json_data):
        response = requests.post(server + '/font/add', json=json_data)
        return json.loads(response.text)

    def consume_new_user(self, json_data):
        response = requests.post(server + '/user/add', json=json_data)
        return json.loads(response.text)

    def consume_update_font(self, json_data):
        response = requests.post(server + '/font/update', json=json_data)
        return json.loads(response.text)

    def get_all_channels(self):
        response = requests.get(server + '/channel/all')
        return json.loads(response.text)

    def get_all_fonts(self):
        response = requests.get(server + '/font/all')
        return json.loads(response.text)

    def get_all_font_styles(self):
        response = requests.get(server + '/font/style/all')
        return json.loads(response.text)

    def get_all_font_languages(self):
        response = requests.get(server + '/language/font/all')
        return json.loads(response.text)

    def get_all_languages(self):
        response = requests.get(server + '/language/all')
        return  json.loads(response.text)

    def validate_user(self, json_data):
        response = requests.post(server + '/user/validate', json=json_data)
        return json.loads(response.text)
