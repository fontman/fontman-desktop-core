""" Session

Session variables and functions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from os.path import expanduser
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# Database session
engine = create_engine(
    'sqlite:///' + expanduser('~') + '/.fontman/fontman.db', echo =True
)
declarative_base().metadata.bind = engine
DBSession = sessionmaker(bind=engine)

db_session = DBSession()
