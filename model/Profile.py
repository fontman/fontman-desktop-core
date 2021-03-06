""" Profile

User profile model

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 22/12/2016
"""

from sqlalchemy import Boolean, Column, Integer, String

from session import Base


class Profile(Base):

    __tablename__ = "profile"

    user_id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    is_logged = Column(Boolean,nullable=False)
    name = Column(String(200), nullable=False)
    password = Column(String(250), nullable=False)
    token = Column(String(250), nullable=False)
