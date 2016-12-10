""" Font language service

manipulate supported languages data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""
from sqlalchemy.orm import contains_eager

from model import FontLanguage, Language
from session import db_session


class FontLanguageService:

    def add_new(self, font_id, language_id):
        new_font_language = FontLanguage(
            font_id=font_id,
            language_id=language_id
        )

        db_session.add(new_font_language)
        db_session.commit()

    def find_all(self):
        return db_session.query(FontLanguage).all()

    def find_by_font_id(self, font_id):
        return db_session.query(FontLanguage).filter_by(font_id=font_id)

    def find_by_language_id(self, language_id):
        return db_session.query(FontLanguage).filter_by(language_id=language_id)
