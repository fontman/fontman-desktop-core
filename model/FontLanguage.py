""" Font language

Keep language information of fonts

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 6/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class FontLanguage(Base):

    __tablename__ = "font_language"

    id = Column(Integer, primary_key=True)
    font_id = Column(String(50), ForeignKey("font.font_id"), nullable=False)
    language_id = Column(Integer, ForeignKey("language.id"), nullable=False)
