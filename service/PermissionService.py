""" Permissions service

High level functions to manipulate data related to user permissions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2017
"""

from model import Permission
from session import db_session


class PermissionService:
    
    def add_new(self, permission_id, entity, entity_id, role):
        new_permission = Permission(
            permission_id=permission_id,
            entity=entity,
            entity_id=entity_id,
            role=role
        )

        db_session.add(new_permission)
        db_session.commit()

        return new_permission

    def delete_by_entity(self, entity):
        self.find_by_entity(entity).delete()
        db_session.commit()

    def delete_by_permission_id(self, permission_id):
        self.find_by_permission_id(permission_id).delete()
        db_session.commit()

    def delete_by_entity_id(self, entity, entity_id):
        self.find_permission(entity, entity_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Permission).all()

    def find_by_entity(self, entity):
        return db_session.query(Permission).filter_by(entity=entity)

    def find_by_entity_id(self, entity, entity_id):
        return db_session.query(Permission).filter_by(
            entity=entity, entity_id=entity_id
        )

    def find_by_permission_id(self, permission_id):
        return db_session.query(Permission).filter_by(permission_id=permission_id)

    def find_permission(self, entity, entity_id):
        return db_session.query(Permission).filter_by(
            entity=entity, entity_id=entity_id
        )

    def update_by_permission_id(self, permission_id, update_data):
        self.find_by_permission_id(permission_id).update(update_data)
