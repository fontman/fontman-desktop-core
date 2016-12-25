""" Font language service

manipulate supported languages data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from model import FontLanguage
from session import db_session


class FontLanguageService:

    def add_new(self, id, font_id, language_id):
        new_font_language = FontLanguage(
            id=id,
            font_id=font_id,
            language_id=language_id
        )

        db_session.add(new_font_language)
        db_session.commit()

    def delete_by_id(self, id):
        self.find_by_id(id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(FontLanguage).all()

    def find_by_id(self, id):
        return db_session.query(FontLanguage).filter_by(id=id)

    def find_by_font_id(self, font_id):
        return db_session.query(FontLanguage).filter_by(font_id=font_id)

    def find_by_language_id(self, language_id):
        return db_session.query(FontLanguage).filter_by(language_id=language_id)

    def is_exists_by_id(self, id):
        try:
            if self.find_by_id(id).one is not None:
                return True

        except:
            return False
