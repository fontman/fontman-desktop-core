""" Team service

High level functions to manipulate teams table.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 4/1/2017
"""

from model import Team
from session import db_session


class TeamService:

    def add_new(self, team_id, name, type):
        new_team = Team(team_id=team_id, name=name, type=type)

        db_session.add(new_team)
        db_session.commit()

        return new_team

    def delete_by_team_id(self, team_id):
        self.find_by_team_id(team_id).delete()
        db_session.commit()

    def find_all(self):
        return db_session.query(Team).all()

    def find_all_team_ids(self):
        return db_session.query(Team.team_id)

    def find_by_team_id(self, team_id):
        db_session.query(Team).filter_by(team_id=team_id)

    def find_by_type(self, type):
        return db_session.query(Team).filter_by(type=type)

    def update_by_team_id(self, team_id, update_data):
        self.find_by_team_id(team_id).update(update_data)
        db_session.commit()
