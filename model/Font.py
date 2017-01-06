""" Font

Basic font information.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from session import Base


class Font(Base):

    __tablename__ = "font"

    font_id = Column(Integer, primary_key=True)
    channel_id = Column(
        Integer, ForeignKey("channel.channel_id"), nullable=False
    )
    installed = Column(Boolean, default=False)
    name = Column(String(200), nullable=False)
    team_id = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)
    upgradable = Column(Boolean, default=False)
