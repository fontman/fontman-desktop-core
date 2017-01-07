""" Team

Collaborative development with a team.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 31/12/2016
"""

from sqlalchemy import Column, Integer, String

from session import Base


class Team(Base):

    __tablename__ = 'team'

    team_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type = Column(String(20), default='public', nullable=False)
