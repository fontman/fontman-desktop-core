""" Language service

High level functions to manipulate language table.

"""


from model import Language
from session import db_session


class LanguageService:

    def add_new(self, tag_id, font_id, language):
        new_tag = Language(
            tag_id=tag_id,
            font_id=font_id,
            language=language
        )

        db_session.add(new_tag)
        db_session.commit()

        return new_tag

    def find_all(self):
        db_session.query(Language).all()

    def find_by_font_id(self, font_id):
        return db_session.query(Language).filter_by(font_id=font_id)
