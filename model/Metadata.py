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
    default_fontface = Column(String(50), nullable=False)
    download_url = Column(String(200), nullable=True)
    license = Column(String(50), nullable=False)
    version = Column(String(20), nullable=True)
