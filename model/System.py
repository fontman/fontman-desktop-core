""" System

Fontman application and operating system related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, Integer, String

from session import Base


class System(Base):

    __tablename__ = "system"

    system_user = Column(String(150), primary_key=True)
    home_directory = Column(String(250), nullable=False)
    font_directory = Column(String(250), nullable=False)
    fontman_home = Column(String(250), nullable=False)
    platform = Column(String(10), nullable=False)
    refresh_rate = Column(Integer, default=1)
    version = Column(String(50), nullable=False)
