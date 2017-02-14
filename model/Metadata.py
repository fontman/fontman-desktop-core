""" Metadata

Font metadata.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 16/1/2017
"""

from sqlalchemy import Column, Integer, String

from session import Base


class Metadata(Base):

    __tablename__ = "metadata"

    metadata_id = Column(Integer, primary_key=True)
    font_id = Column(Integer, nullable=False)
    latest_tag_url = Column(String(200), nullable=False)
    tags_url = Column(String(200), nullable=False)
