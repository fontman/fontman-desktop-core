""" Core service

High level functions to manipulate fontman application and operating system
related data.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/12/2016
"""

from model import System
from session import db_session


class SystemService:

    def add_new(
            self,
            home_directory,
            fontman_home,
            platform,
            refresh_rate,
            system_user,
            version
    ):
        new_system = System(
            home_directory=home_directory,
            fontman_home=fontman_home,
            platform=platform,
            refresh_rate=refresh_rate,
            system_user=system_user,
            version=version
        )

        db_session.add(new_system)
        db_session.commit()

    def find_system_info(self):
        return db_session.query(System).first()
