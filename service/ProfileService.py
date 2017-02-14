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

    def delete_all(self):
        self.find_all().delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Profile)

    def find_by_email(self, email):
        return db_session.query(Profile).filter_by(email=email).first()

    def find_by_user_id(self, user_id):
        return db_session.query(Profile).filter_by(user_id=user_id)

    def find_logged_user(self):
        return db_session.query(Profile).filter_by(is_logged=True).first()

    def set_active_mode(self, user_id, active_mode):
        self.update_by_user_id(
            user_id,
            {
                "is_logged": active_mode
            }
        )

    def update_by_user_id(self, user_id, update_list):
        self.find_by_user_id(user_id).update(update_list)
        db_session.commit()
