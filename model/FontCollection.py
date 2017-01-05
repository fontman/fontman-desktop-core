""" Font collection

Table to track font list of a collection.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/1/2017
"""

from sqlalchemy import Column, ForeignKey, Integer

from session import Base


class FontCollection(Base):

    __tablename__ = 'font_collection'

    font_collection_id = Column(Integer, primary_key=True)
    collection_id = Column(
        Integer, ForeignKey('collection.collection_id'), nullable=False
    )
    font_id = Column(Integer, ForeignKey('font.font_id'), nullable=False)
