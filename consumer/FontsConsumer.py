""" Fontman server fonts consumer

Consume and sync with fontman server fonts REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from service import MetadataService
from session import api_base_url

import json, requests


class FontsConsumer:
    
    def consume_all_fonts(self):
        response = requests.get(api_base_url + "/fonts")
        return json.loads(response.text)
    
    def consume_by_font_id(self, font_id):
        response = requests.get(api_base_url + "/fonts/" + str(font_id))
        return json.loads(response.text)
    
    def consume_by_query(self, team_id="", type=""):
        query_string = "/?"

        if team_id is not "":
            query_string += "team_id=" + str(team_id) + "&"

        if type is not "":
            query_string += "type=" + type + "&"

        response = requests.get(
            api_base_url + "/fonts" + query_string
        )
        return json.loads(response.text)

    def consume_delete_font(self, font_id, json_data):
        response = requests.post(
            api_base_url + "/fonts/" + str(font_id) + "/delete",
            json=json_data
        )
        return json.loads(response.text)

    def consume_metadata_by_font_id(self, font_id):
        response = requests.get(
            api_base_url + "/fonts/" + str(font_id) + "/metadata"
        )
        return json.loads(response.text)
    
    def consume_new_font(self, json_data):
        response = requests.post(api_base_url + "/fonts/new", json=json_data)
        return json.loads(response.text)

    def consume_latest_rel_info(self, font_id):
        response = json.loads(requests.get(
            api_base_url + "/fonts/" + str(font_id) + "/latest"
        ))
        return json.loads(requests.get(response["rel_info_url"]))

    def consume_rel_info(self, font_id, rel_id):
        response = json.loads(requests.get(
            api_base_url + "/fonts/" + str(font_id) + "/releases/" + str(rel_id)
        ).text)
        return json.loads(requests.get(response["rel_info_url"]).text)

    def consume_releases(self, font_id):
        response = json.loads(requests.get(
            MetadataService().find_by_font_id(font_id).first().tags_url
        ).text)
        return response
    
    def consume_update_font(self, font_id, json_data):
        response = requests.post(
            api_base_url + "/fonts/" + str(font_id) + "/update",
            json=json_data
        )
        return json.loads(response.text)
