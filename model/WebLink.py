""" Web link

Provides cdn/web links for the font files.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 5/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class WebLink(Base):

    __tablename__ = 'web_link'

    id = Column(Integer, primary_key=True)
    file_name = Column(String(250), nullable=False)
    font_id = Column(String(50), ForeignKey("font.font_id"), nullable=False)
    style = Column(String(50), nullable=False)
    type = Column(String(10), nullable=False)
    web_link = Column(String(250), nullable=False)
