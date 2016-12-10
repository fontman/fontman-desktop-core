""" Font file service

Provides high level functions to manipulate font file table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/12/2016
"""

from model import FontFile
from session import db_session


class FontFileService:

    def add_new(self, file_name, font_id, type):
        new_font_file = FontFile(
            file_name =file_name,
            font_id = font_id,
            type=type
        )

        db_session.add(new_font_file)
        db_session.commit()

    def delete_by_file_name(self, file_name, font_id):
        self.find_by_file_name(file_name, font_id).delete()
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_all_by_font_id(font_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(FontFile).all()

    def find_all_by_font_id(self, font_id):
        return db_session.query(FontFile).filter_by(font_id=font_id)

    def find_by_file_name(self, file_name, font_id):
        return db_session.query(FontFile).filter_by(
            file_name=file_name, font_id=font_id
        )
