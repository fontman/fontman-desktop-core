""" Profile service

High level functions to manipulate profile data

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 22/12/2016
"""

from model import Profile
from session import db_session


class ProfileService:

    def add_new(self, user_id, email, name, password, token):
        new_profile = Profile(
            user_id=user_id,
            email=email,
            is_logged=True,
            name=name,
            password=password,
            token=token,
        )

        db_session.add(new_profile)
        db_session.commit()

        return new_profile

    def find_user(self):
        try:
            return db_session.query(Profile).first()
        except:
            return None

    def set_active_mode(self, active_mode):
        self.update_user(
            {
                "is_active": active_mode
            }
        )

    def update_user(self, update_list):
        self.find_user().update(update_list)
        db_session.commit()
