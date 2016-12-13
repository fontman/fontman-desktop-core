""" GitLab consumer

Helps to access GitLab API to gather data.
Uses python requests library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 12/12/2016
"""

import requests


class GitLabConsumer:

    def __init__(self, branch, host, repo_id, repository, private_token, user):
        self.__branch = branch
        self.__host = host
        self.__private_token = private_token
        self.__repo_id = repo_id
        self.__repository = repository
        self.__user = user

    def get_cdn_link(self, file_path):
        return self.__host + "/"\
               + self.__user + "/"\
               + self.__repository + "/raw/"\
               + self.__branch + "/"\
               + file_path

    def get_latest_release_info(self):
        return requests.get(
            self.__host + "/api/v3/projects/"
            + self.__repo_id + "/" + "/repository/tags/?private="
            + self.__private_token
        ).json()[0]

    def get_release_link(self, tag_name):
        return self.__host + "/" + self.__user + "/"\
               + self.__branch + "/" + "repository/archive.zip?ref="\
               + tag_name + "&private_token="\
               + self.__private_token

    def list_tags(self):
        return requests.get(
            self.__host + "/api/v3/projects/"
            + self.__repo_id + "/repository/tags"
        ).json()
