""" Font

Basic font information.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, ForeignKey, String

from session import Base


class Font(Base):

    __tablename__ = "font"

    font_id = Column(String(50), primary_key=True)
    channel_id = Column(
        String(10), ForeignKey("channel.channel_id"), nullable=False
    )
    file_name = Column(String(250), nullable=False)
    installed = Column(Boolean, default=False)
    name = Column(String(150), nullable=False)
    url = Column(String(250), nullable=True)
    upgradable = Column(Boolean, default=False)
    version = Column(String(30), nullable=False)
