""" Initializer

Initialize system directories, files and database.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from service import SystemService
from session import Base, version
from utility import FileManager

import os, getpass, platform
from os.path import expanduser
from sqlalchemy import create_engine


def initialize():
    # create fontman data directories
    FileManager().create_directory("./data")

    # create database
    engine = create_engine(
        "sqlite:///./data/fontman.db"
    )
    Base.metadata.create_all(engine, checkfirst=True)

    # gather and save system data
    user_home_dir = expanduser("~")
    system = platform.system()
    sys_font_dir = ""

    if "Windows" in system:
        sys_font_dir = "C:\\Windows\\Fonts"

    elif "Linux" in system:
        sys_font_dir = user_home_dir + "/.fonts"

    else:
        system = "mac"
        sys_font_dir = user_home_dir + "/Library/Fonts"

    SystemService().add_new(
        user_home_dir,
        sys_font_dir,
        os.getcwd() + "/data",
        system,
        1,
        getpass.getuser(),
        version
    )

