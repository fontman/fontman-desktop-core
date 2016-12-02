""" Initializer

Initialize system directories, files and create appropriate sessions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""
import os, platform
from os.path import expanduser


class Initializer:

    def __init__(self):
        self.__home_directory = expanduser("~")

    def cached_data_directory(self):
        return self.__home_directory + "/.fontman/cached_data"

    def fontman_directory(self):
        return self.__home_directory + "/.fontman"

    def system_font_directory(self):
        font_dir = ""
        system = platform.system()

        if "linux" in system.lower():
            font_dir = self.__home_directory + "/.fonts"
        elif "osx" in system.lower():
            font_dir = self.__home_directory + "/Library/Fonts"
        elif "windows" in system.lower():
            font_dir = os.environ["SYSTEMDRIVE"] + "\\\\Windows\\Fonts"
