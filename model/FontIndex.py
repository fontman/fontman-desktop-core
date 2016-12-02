""" Font index

This model helps to track installed fonts and available updates quickly.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base


class FontIndex(declarative_base()):

    __tablename__ = 'font_index'

    font_id = Column(String(50), ForeignKey('font.font_id'), primary_key=True)
    installed = Column(Boolean, default=False)
    upgradable = Column(Boolean, default=False)
