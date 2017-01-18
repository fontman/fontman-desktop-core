""" Fontman server collections consumer

Consume and sync with fontman server collections REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class CollectionsConsumer:

    def consume_all_collections(self):
        response = requests.get(api_base_url + "/collections")
        return json.loads(response.text)

    def consume_by_collection_id(self, collection_id):
        response = requests.get(
            api_base_url + "/collections/" + str(collection_id)
        )
        return json.loads(response.text)

    def consume_by_query(self, team_id="", type=""):
        query_string = "/?"

        if team_id is not "":
            query_string += "team_id=" + str(team_id) + "&"

        if type is not "":
            query_string += "type=" + type + "&"

        response = requests.get(
            api_base_url + "/collections" + query_string
        )
        return json.loads(response.text)

    def consume_new_collection(self, json_data):
        response = requests.post(
            api_base_url + "/collections/new", json=json_data
        )
        return json.loads(response.text)

    def consume_delete_collection(self, collection_id, json_data):
        response = requests.post(
            api_base_url + "/collections/" + str(collection_id) + "/delete",
            json=json_data
        )
        return json.loads(response.text)

    def consume_update_collection(self, collection_id, json_data):
        response = requests.post(
            api_base_url + "/collections/" + str(collection_id) + "/update",
            json=json_data
        )
        return json.loads(response.text)
