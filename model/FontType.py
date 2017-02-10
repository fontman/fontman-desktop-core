""" Font Type

Characteristics of a font. eg: serif/sans serif

Created by Lahiru Pathirage @ Mooniak <lpsandaruwan@gmail.com> on 8/2/2017
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from session import Base


class FontType(Base):

    __tablename__ = "fonttype"

    type_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey("font.font_id"))
    tag = Column(String(20), nullable=False)
