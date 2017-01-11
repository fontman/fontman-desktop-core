""" Fontman server channels consumer

Consume and sync with fontman server channels REST API.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 9/1/2017
"""

from session import api_base_url

import json, requests


class ChannelsConsumer:

    def consume_all_channels(self):
        response = requests.get(api_base_url + "/channels")
        return json.loads(response)
