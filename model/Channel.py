""" Channel

Available font channels

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, String

from session import Base


class Channel(Base):

    __tablename__ = 'channel'

    channel_id = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    key = Column(String(200), nullable=True)
    type = Column(String(20), nullable=False)
