""" Font

Basic font information service.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import Font
from session import db_session


class FontService:

    def add_new(self, font_id, channel_id, name, type):
        new_font = Font(
            font_id=font_id,
            channel_id = channel_id,
            is_chosen = False,
            is_installed=False,
            is_upgradable=False,
            name=name,
            type=type,
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
        try:
            if self.find_by_font_id(font_id).one() is not None:
                return True
        except:
            return False

    def update_all(self, update_list):
        self.find_all().update(update_list)
        db_session.commit()

    def update_by_font_id(self, font_id, update_list):
        self.find_by_font_id(font_id).update(update_list)
        db_session.commit()
