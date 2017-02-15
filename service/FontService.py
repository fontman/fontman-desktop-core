""" Font

Basic font information service.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import Font
from session import db_session


class FontService:

    def add_new(self, font_id, name):
        new_font = Font(
            font_id=font_id,
            is_chosen = False,
            is_installed=False,
            is_upgradable=False,
            name=name
        )

        db_session.add(new_font)
        db_session.commit()

        return new_font

    def find_all(self):
        return db_session.query(Font).all()

    def find_all_chosen(self):
        return db_session.query(Font).filter_by(is_chosen=True)

    def find_all_font_ids(self):
        return db_session.query(Font.font_id)

    def find_all_installable(self):
        return db_session.query(Font).filter_by(is_installed=False)

    def find_all_installed(self):
        return db_session.query(Font).filter_by(is_installed=True)

    def find_all_upgradable(self):
        return db_session.query(Font).filter_by(is_upgradable=True)

    def find_by_channel_id(self, channel_id):
        return db_session.query(Font).filter_by(channel_id=channel_id)

    def find_by_font_id(self, font_id):
        return db_session.query(Font).filter_by(font_id=font_id)

    def is_exists_by_font_id(self, font_id):
        if self.find_by_font_id(font_id).first() is None:
            return False
        else:
            return True

    def update_all(self, update_data):
        self.find_all().update(update_data)

    def update_by_font_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        db_session.commit()
