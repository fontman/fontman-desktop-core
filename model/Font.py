""" Font

Basic font information.

Created by Lahiru Pathirage <lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, Integer, String

from session import Base


class Font(Base):

    __tablename__ = "font"

    font_id = Column(Integer, primary_key=True)
    is_chosen = Column(Boolean, default=False)
    is_installed = Column(Boolean, default=False)
    is_upgradable = Column(Boolean, default=False)
    name = Column(String(200), nullable=False)
