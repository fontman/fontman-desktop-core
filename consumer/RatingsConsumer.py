""" Fontman server ratings consumer

Consume and sync with fontman server ratings REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class RatingsConsumer:

    def consume_by_entity_id(self, entity, entity_id):
        response = requests.get(
            api_base_url + '/ratings/' + entity + '/' + entity_id
        )
        return json.loads(response.text)

    def consume_new_rating(self, json_data):
        response = requests.post(
            api_base_url + '/ratings/new', json=json_data
        )
        return json.loads(response.text)

    def consume_delete_rating(self, rating_id, json_data):
        response = requests.post(
            api_base_url + '/ratings/' + rating_id + '/delete',
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_rating(self, rating_id, json_data):
        response = requests.post(
            api_base_url + '/ratings/' + rating_id + '/update',
            json=json_data
        )
        return json.loads(response.text)
