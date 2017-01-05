""" Font-faces srvice

High level functions to manipulate font faces table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import FontFace
from session import db_session


class FontFaceService:

    def add_new_font(self, fontface_id, fontface, font_id, resource_path):
        new_fontface = FontFace(
            fontface_id=fontface_id,
            fontface=fontface,
            font_id=font_id,
            resource_path=resource_path
        )

        db_session.add(new_fontface)
        db_session.commit()

        return new_fontface

    def delete_by_fontface_id(self, fontface_id):
        self.find_by_fontface_id(fontface_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(FontFace).all()

    def find_by_fontface_id(self, fontface_id):
        return db_session.query(FontFace).filter_by(fontface_id=fontface_id)

    def find_by_font_id(self, font_id):
        return db_session.query(FontFace).filter_by(font_id=font_id)

    def update_by_fontface_id(self, fontface_id, update_data):
        self.find_by_fontface_id(fontface_id).update(update_data)
        db_session.commit()
