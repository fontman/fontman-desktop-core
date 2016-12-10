""" Installed Fonts

Installed fonts information directory.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import datetime
from sqlalchemy import Column, Date, ForeignKey, String

from session import Base


class InstalledFont(Base):

    __tablename__ = 'installed_font'

    font_id = Column(String(50), ForeignKey('font.font_id'), primary_key=True)
    date = Column(Date, onupdate=datetime.datetime.now())
    version = Column(String(30), nullable=False)
