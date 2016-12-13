""" Language service

Supported language type details

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from model import Language
from session import db_session


class LanguageService:

    def add_new(self, is_enabled, value):
        new_language = Language(is_enabled=is_enabled, value=value)

        db_session.add(new_language)
        db_session.commit()

    def find_all(self):
        return db_session.query(Language).all()

    def find_all_enabled(self):
        return db_session.query(Language).filter_by(is_enabled=True).all()

    def find_by_id(self, id):
        return db_session.query(Language).filter_by(id=id)

    def find_by_value(self, value):
        print(value)
        return db_session.query(Language).filter_by(value=value)

    def update_by_id(self, id, update_list):
        self.find_by_id(id).update(update_list)
        db_session.commit()

    def update_by_value(self, value, update_list):
        self.find_by_value(value).update(update_list)
        db_session.commit()
