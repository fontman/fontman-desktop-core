""" Metadata service

CRUD operations on font metadata.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 16/1/2017
"""

from model import Metadata
from session import db_session


class MetadataService:

    def add_new(self, font_id, latest_tag_url, tags_url):
        new_metadata = Metadata(
            font_id=font_id,
            latest_tag_url=latest_tag_url,
            tags_url=tags_url
        )

        db_session.add(new_metadata)
        db_session.commit()

        return new_metadata

    def delete_by_metadata_id(self, metadata_id):
        self.find_by_metadata_id(metadata_id).delete()
        db_session.commit()

    def delete_by_font_id(self, font_id):
        self.find_by_font_id(font_id)
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(Metadata).filter_by(font_id=font_id)

    def find_by_metadata_id(self, metadata_id):
        return db_session.query(Metadata).filter_by(metadata_id=metadata_id)
