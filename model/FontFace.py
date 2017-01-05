""" Font faces

Table to keep font faces data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class FontFace(Base):

    __tablename__ = 'fontface'

    fontface_id = Column(Integer, primary_key=True)
    fontface = Column(String(100), nullable=False)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    resource_path = Column(String(250), nullable=False)
