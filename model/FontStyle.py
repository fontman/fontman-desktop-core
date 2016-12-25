""" Font styles

Font styles information

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 18/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class FontStyle(Base):

    __tablename__ = 'font_style'

    style_id = Column(Integer, primary_key=True)
    cdn = Column(String(250), nullable=False)
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
    style = Column(String(50), nullable=False)
