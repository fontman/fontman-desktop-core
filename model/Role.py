""" Permissions table

Store user permission data as cache.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/1/2017
"""

from sqlalchemy import Column, Integer, String

from session import Base


class Role(Base):

    __tablename__ = "role"

    role_id = Column(Integer, primary_key=True)
    entity_id = Column(Integer, nullable=False)
    entity = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False)
