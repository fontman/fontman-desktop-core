""" Github font service

High level functions to manipulate font information related to github hosted
fonts in database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import GithubFont
from session import db_session


class GithubFontService:

    def add_new(self, font_id, branch, path, repo_name, user):
        new_github_font = GithubFont(
            font_id=font_id,
            branch=branch,
            path=path,
            repo_name=repo_name,
            user=user
        )

        db_session.add(new_github_font)
        db_session.commit()

    def find_by_font_id(self, font_id):
        return db_session.query(GithubFont).filter_by(font_id=font_id)

    def find_all(self):
        return db_session.query(GithubFont).all()

    def update_by_font_id(self, font_id, attribute, value):
        self.find_by_font_id(font_id).update({attribute: value})
