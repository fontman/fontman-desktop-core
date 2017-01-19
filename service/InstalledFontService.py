""" Installed fonts service

High level functions to manipulate data related to installed fonts information
in database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import InstalledFont
from session import db_session


class InstalledFontService:

    def add_new(self, font_id, version):
        new_installed_font = InstalledFont(
            font_id=font_id,
            version=version
        )

        db_session.add(new_installed_font)
        db_session.commit()

        return new_installed_font

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id).delete()
        db_session.commit()

    def find_all(self):
        db_session.query(InstalledFont).all()

    def find_by_font_id(self, font_id):
        return db_session.query(InstalledFont).filter_by(font_id=font_id)

    def update_by_font_id(self, font_id, update_list):
        self.find_by_font_id(font_id).update(update_list)
        db_session.commit()
