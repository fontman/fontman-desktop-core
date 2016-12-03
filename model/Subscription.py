""" Subscription

Subscription credentials related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, String

from session import Base


class Subscription(Base):

    __tablename__ = 'subscription'

    user_id = Column(String(50), primary_key=True)
    username = Column(String(100), nullable=False)
    name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)
    secret = Column(String(250), nullable=False)
