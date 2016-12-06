""" Web link service

Provides cdn/web links for the font files.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/12/2016
"""

from model import WebLink
from session import db_session


class WebLinkService:

    def add_new(self, file_name, font_id, style, type, web_link):
        new_web_link = WebLink(
            file_name=file_name,
            font_id=font_id,
            style=style,
            type=type,
            web_link=web_link
        )

        db_session.add(new_web_link)
        db_session.commit()

    def find_all(self):
        return db_session.query(WebLink).all()

    def find_by_file_name(self, file_name, font_id):
        return db_session.query(WebLink).filter_by(
            file_name=file_name,
            font_id=font_id
        )

    def find_by_style(self, font_id, style):
        return db_session.query(WebLink).filter_by(
            font_id = font_id,
            style=style
        )

    def find_all_by_font_id(self, font_id):
        return db_session.query(WebLink).filter_by(font_id=font_id).all()

    def update_by_file_name(self, font_id, file_name, update_list):
        db_session.query(font_id=font_id, file_name=file_name).update(
            update_list
        )
