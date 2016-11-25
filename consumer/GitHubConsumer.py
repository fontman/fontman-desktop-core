""" GitHub consumer

Helps to access GitHub API to gather data, download data and generate cdn links
for appropriate fonts.
Uses requests library.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 26/11/2016
"""

import requests


class GitHubConsumer:

    def __init__(self, branch, repository, user):
        self.__branch = branch
        self.__repository = repository
        self.__user = user

    def get_cdn_link(self, file_path, file_name):
        return 'https://cdn.rawgit.com/' + self.__user + '/' + \
               self.__repository + '/' + self.__branch + '/' + file_path\
               + '/' + file_name

    def download_file(self, destination, download_link):
        with open(destination, 'wb') as stream:
            stream.write(requests.get(download_link).content)

    def list_contents(self, location=''):
        return requests.get('https://api.github.com/repos/'
                            + self.__user + '/'
                            + self.__repository + '/contents/'
                            + location + '?ref='
                            + self.__branch).json()
