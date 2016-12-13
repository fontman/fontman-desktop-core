""" GitLab font

Font information related to github hosted fonts.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 13/12/2016
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from session import Base


class GitLabFont(Base):

    __tablename__ = "gitlab_font"

    font_id = Column(String(50), ForeignKey("font.font_id"), primary_key=True)
    host = Column(String(100), nullable=False)
    private_token = Column(String(250), nullable=False)
    repo_id = Column(Integer, nullable=False)
    repository = Column(String(100), nullable=False)
    style_branch = Column(String(100), nullable=False)
    style_path = Column(String(250), nullable=False)
    user = Column(String(100), nullable=False)
