""" Subscription service

High level functions to manipulate subscription credentials related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import Subscription
from session import db_session


class SubscriptionService:

    def add_new(self, user_id, username, name, email, secret):
        new_subscription = Subscription(
            user_id=user_id,
            username =username,
            name=name,
            email=email,
            secret=secret
        )

        db_session.add(new_subscription)
        db_session.commit()

    def delete_by_username(self, username):
        self.find_by_user_name(username).delete()
        db_session.commit()

    def find_all(self):
        db_session.query(Subscription).all()

    def find_by_user_name(self, username):
        db_session.query(Subscription).filter_by(username=username)

    def update_by_username(self, username, attribute, value):
        self.find_by_user_name(username).update({attribute: value})
        db_session.commit()
