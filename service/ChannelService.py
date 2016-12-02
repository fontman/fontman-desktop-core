""" Channel Service

Available font channels, service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import Channel
from session import db_session


class ChannelService:

    def add_new(self, channel_id, base_url, type, license_key=None):

        new_channel = Channel(
            channel_id=channel_id,
            base_url=base_url,
            is_active=True,
            license_key=license_key,
            type=type
        )

        db_session.add(new_channel)
        db_session.commit()

    def find_by_channel_id(self, channel_id):
        return db_session.query(Channel).filter_by(channel_id=channel_id)

    def find_all(self):
        return db_session.query(Channel).all()

    def update_by_channel_id(self, channel_id, attribute, value):
        self.find_by_channel_id(channel_id).update({attribute: value})
