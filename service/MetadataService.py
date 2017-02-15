""" Metadata service

CRUD operations on font metadata.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 16/1/2017
"""

from model import Metadata
from session import db_session


class MetadataService:

    def add_new(
            self,
            metadata_id,
            font_id,
            default_fontface,
            download_url,
            license,
            version
    ):
        new_metadata = Metadata(
            metadata_id=metadata_id,
            font_id=font_id,
            default_fontface=default_fontface,
            download_url=download_url,
            license=license,
            version=version
        )

        db_session.add(new_metadata)
        db_session.commit()

        return new_metadata

    def delete_by_metadata_id(self, metadata_id):
        self.find_by_font_id(metadata_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Metadata)

    def find_by_font_id(self, font_id):
        return db_session.query(Metadata).filter_by(
            font_id=font_id
        )

    def update_by_font_id(self, font_id, update_data):
        self.find_by_font_id(font_id).update(update_data)
        db_session.commit()
