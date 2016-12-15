""" GitHub font

Font information related to github hosted fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import Column, ForeignKey, String

from session import Base


class GitHubFont(Base):

    __tablename__ = 'github_font'

    font_id = Column(String(50), ForeignKey('font.font_id'), primary_key=True)
    repo_name = Column(String(250), nullable=False)
    style_branch = Column(String(100), nullable=False)
    style_path = Column(String(250), nullable=False)
    user = Column(String(100), nullable=False)