""" Channel

Available font channels

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, String

from session import Base


class Channel(Base):

    __tablename__ = 'channel'

    channel_id = Column(String(50), primary_key=True)
    base_url = Column(String(250), nullable=False)
    is_active = Column(Boolean, default=True)
    license_key = Column(String(250), nullable=True)
    type = Column(String(10), nullable=False)
