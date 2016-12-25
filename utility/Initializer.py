""" Initializer

Initialize system directories, files and database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

import os, getpass, platform
from os.path import expanduser
from sqlalchemy import create_engine

from service import SystemService
from session import Base, version
from utility import FileManager


def initialize():

    # home directory
    home_directory = expanduser("~")

    # operating system
    system = platform.system()

    # system font directory
    font_directory = ""

    # fontman home directory
    fontman_home = "data"

    # set system font directory considering operating system type
    if "linux" in system.lower():
        font_directory = home_directory + "/.fonts"
    elif "osx" in system.lower():
        font_directory = home_directory + "/Library/Fonts"
    elif "windows" in system.lower():
        font_directory = os.environ["SYSTEMDRIVE"] + "\\\\Windows\\Fonts"

    # create directories
    file_manager = FileManager()

    file_manager.create_directory(fontman_home)
    file_manager.create_directory(fontman_home + "/temp")
    file_manager.create_directory(fontman_home + "/temp/extracted")

    # create database
    engine = create_engine(
        "sqlite:///./data/fontman.db"
    )
    Base.metadata.create_all(engine)

    # write application initial data
    SystemService().add_new(
        home_directory,
        font_directory,
        fontman_home,
        system,
        "1h",
        getpass.getuser(),
        version
    )
