""" Font types service

High level functions to manipulate font types table

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 8/2/2017
"""

from model import FontType
from session import db_session


class FontTypeService:

    def add_new(self, font_id, tag):
        new_tag = FontType(
            font_id=font_id,
            tag=tag
        )

        db_session.add(new_tag)
        db_session.commit()

        return new_tag

    def find_all(self):
        return db_session.query(FontType).all()

    def find_by_font_id(self, font_id):
        return db_session.query(FontType).filter_by(font_id=font_id)

    def find_by_tag(self, tag):
        return db_session.query(FontType).filter_by(tag=tag)

    def find_by_type_id(self, type_id):
        return db_session.query(FontType).filter_by(type_id=type_id)
