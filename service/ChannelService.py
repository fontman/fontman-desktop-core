""" Channel Service

Available font channels, service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import Channel
from session import db_session


class ChannelService:

    def add_new(self, channel_id, name, type, key=None):
        new_channel = Channel(
            channel_id=channel_id,
            is_active=True,
            key=key,
            name=name,
            type=type
        )

        db_session.add(new_channel)
        db_session.commit()

    def delete_by_channel_id(self, channel_id):
        self.find_by_channel_id(channel_id).delete()
        db_session.commit()

    def find_by_channel_id(self, channel_id):
        return db_session.query(Channel).filter_by(channel_id=channel_id)

    def find_enabled_by_channel_id(self, channel_id):
        try:
            return db_session.query(Channel).filter_by(
                channel_id=channel_id, is_active=True
            ).one().is_active
        except:
            return False

    def find_all(self):
        return db_session.query(Channel).all()

    def find_by_channel_type(self, type):
        return db_session.query(Channel).filter_by(type=type).all()

    def is_exists_by_id(self, channel_id):
        try:
            if self.find_by_channel_id(channel_id).one() is not None:
                return True
        except:
            return False

    def update_by_channel_id(self, channel_id, update_list):
        self.find_by_channel_id(channel_id).update(update_list)
        db_session.commit()
