""" Fontman server fonts consumer

Consume and sync with fontman server fonts REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/1/2017
"""

from session import api_base_url

import json, requests


class FontsConsumer:
    
    def consume_all_fonts(self):
        response = requests.get(api_base_url + "/fonts")
        return json.loads(response.text)
    
    def consume_by_font_id(self, font_id):
        response = requests.get(api_base_url + "/fonts/" + str(font_id))
        return json.loads(response.text)
