""" Permissions table

Store user permission data as cache.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from sqlalchemy import Column, Integer, String

from session import Base


class Permission(Base):

    __tablename__ = 'permission'

    permission_id = Column(Integer, primary_key=True)
    entity = Column(String(20), nullable=False)
    entity_id = Column(Integer, nullable=False)
    role = Column(String(20), nullable=False)
