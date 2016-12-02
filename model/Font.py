""" Font

Basic font information.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


class Font(declarative_base()):

    __tablename__ = 'font'

    font_id = Column(String(50), primary_key=True)
    channel_id = Column(
        String(10), ForeignKey('channel.channel_id'), nullable=False
    )
    name = Column(String(150), nullable=False)
    version = Column(String(30), nullable=False)
