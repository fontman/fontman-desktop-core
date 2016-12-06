""" Font file

Keep installed font files information

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class FontFile(Base):

    __tablename__ = "font_file"

    id = Column(Integer, primary_key=True)
    file_name = Column(String(250), nullable=False)
    font_id = Column(String(50), ForeignKey("font.font_id"), nullable=False)
    style = Column(String(50), nullable=False)
    type = Column(String(10), nullable=False)
