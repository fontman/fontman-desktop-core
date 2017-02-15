""" Metadata service

Consume metadata of fonts from fontman server REST API.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 15/2/2017
"""

from session import api_base_url

import json, requests


class TagsConsumer:

    def consume_by_font_id(self, font_id):
        response = requests.get(api_base_url + "/tags/" + str(font_id))
        return json.loads(response.text)
