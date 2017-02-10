""" Fontman server tags consumer

Consume and sync with fontman server roles REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class TagsConsumer:

    def consume_tags_by_font_id(self, font_id):
        response = requests.get(api_base_url + "/tags/" + str(font_id))
        return json.loads(response)
