""" Collections service

Provides high level functions to manipulate font collections table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/2/2017
"""

from model import Collection
from session import db_session


class CollectionService:

    def add_new(self, name, type):
        new_collection = Collection(
            name=name,
            type=type
        )

        db_session.add(new_collection)
        db_session.commit()

        return new_collection

    def delete_by_collection_id(self, collection_id):
        self.find_by_collection_id(collection_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Collection).all()

    def find_all_collection_ids(self):
        return db_session.query(Collection.collection_id)

    def find_by_collection_id(self, collection_id):
        return db_session.query(Collection).filter_by(
            collection_id=collection_id
        )

    def find_by_team_id(self, team_id):
        return db_session.query(Collection).filter_by(team_id=team_id)

    def find_by_type(self, type):
        return db_session.query(Collection).filter_by(type=type)

    def update_by_collection_id(self, collection_id, update_data):
        self.find_by_collection_id(collection_id).update(update_data)
        db_session.commit()
