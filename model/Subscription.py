""" Subscription

Subscription credentials related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class Subscription(declarative_base()):

    __tablename__ = 'system'

    user_id = Column(String(50), primary_key=True)
    username = Column(String(100), nullable=False)
    name = Column(String(250), nullable=True)
    email = Column(String(250), nullable=False)
    secret = Column(String(250), nullable=False)
