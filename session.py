""" session

Session variables and functions.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool


# fontman server
server = "http://127.0.0.1:8080"

# fontman version
version = '0.1.0-SNAPSHOT'

# Database session variables
engine = create_engine(
    'sqlite:///./data/fontman.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool, echo=True,
)
Base = declarative_base()

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

db_session = DBSession()

# db lock
db_lock = False
