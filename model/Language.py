""" Font language

Supported language types

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class Language(Base):

    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    value = Column(String(100), nullable=False)
