""" GitLab font service

High level functions to manipulate font information related to github hosted
fonts in database

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import GitLabFont
from session import db_session


class GitLabFontService:

    def add_new(self,
                font_id,
                host,
                private_token,
                repo_id,
                repository,
                style_branch,
                style_path,
                user
                ):
        new_gitlab_font = GitLabFont(
            font_id=font_id,
            host=host,
            private_token=private_token,
            repo_id=repo_id,
            repository=repository,
            style_branch=style_branch,
            style_path=style_path,
            user=user
        )

        db_session.add(new_gitlab_font)
        db_session.commit()

    def find_all(self):
        return db_session.query(GitLabFont).all()

    def find_by_font_id(self, font_id):
        return db_session.query(GitLabFont).filter_by(font_id=font_id)

    def update_by_font_id(self, font_id, update_list):
        self.find_by_font_id(font_id).update(update_list)
        db_session.commit()
