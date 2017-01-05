""" Fontman server font faces consumer

Consume and sync with fontman server font faces REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class FontFacesConsumer:
    
    def consume_all_fontfaces(self):
        response = requests.get(api_base_url + '/fontfaces')
        return json.loads(response.text)

    def consume_by_fontface_id(self, fontface_id):
        response = requests.get(api_base_url + '/fontfaces/' + fontface_id)
        return json.loads(response.text)

    def consume_by_query(self, font_id):
        response = requests.get(
            api_base_url + '/fontfaces/?font_id=' + font_id
        )
        return json.loads(response.text)

    def consume_delete_fontface(self, fontface_id, json_data):
        response = requests.post(
            api_base_url + '/fontfaces/' + fontface_id + '/delete',
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_fontface(self, fontface_id, json_data):
        response = requests.post(
            api_base_url + '/fontfaces/' + fontface_id + '/update',
            json=json_data
        )
        return json.loads(response.text)
