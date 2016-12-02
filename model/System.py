""" System

Fontman application and operating system related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base


class System(declarative_base()):

    __tablename__ = 'system'

    home_directory = Column(String(250), nullable=False)
    fontman_home = Column(String(250), nullable=False)
    platform = Column(String(10), nullable=False)
    refresh_rate = Column(String(5), default='1h', nullable=False)
    system_user = Column(String(150), nullable=False)
    version = Column(String(50), nullable=False)
