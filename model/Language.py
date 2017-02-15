""" Language

Languages of fonts.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 15/2/2017
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from session import Base


class Language(Base):

    __tablename__ = "language"

    tag_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey("font.font_id"), nullable=False)
    language = Column(String(15), nullable=False)
