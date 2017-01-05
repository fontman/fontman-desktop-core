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

    # create database
    engine = create_engine(
        "sqlite:///./data/fontman.db"
    )
    Base.metadata.create_all(engine)
