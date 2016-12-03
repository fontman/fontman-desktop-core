""" Font index service

Provides high level functions to manipulate indexed data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import FontIndex
from session import db_session


class FontIndexService:

    def add_new(self, font_id, installed, upgradable):
        new_font_index = FontIndex(
            font_id=font_id,
            installed=installed,
            upgradable=upgradable
        )

        db_session.add(new_font_index)
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(FontIndex).filter_by(font_id=font_id).one()

    def find_all(self):
        return db_session.query(FontIndex).all()

    def find_all_installable(self):
        return db_session.query(FontIndex).filter_by(installed=False)

    def find_all_installed(self):
        return db_session.query(FontIndex).filter_by(installed=True)

    def find_all_upgradable(self):
        return db_session.query(FontIndex).filter_by(upgradable=True)

    def update_by_font_id(self, font_id, attribute, value):
        self.find_by_font_id(font_id).update({attribute: value})
