""" Font language

Supported language types

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from session import Base


class Language(Base):

    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    is_enabled = Column(Boolean, nullable=False)
    value = Column(String(100), nullable=False)
