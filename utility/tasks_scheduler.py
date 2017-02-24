""" Tasks scheduler

Schedule and run tasks on threads.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 2/2/2017
"""

from service import SystemService
from utility import CacheManager
from utility import FileManager

import time


def run_tasks():
    while True:
        print("Preparing to update font cache")

        FileManager().create_file("./data/db.lock", "on")
        time.sleep(5)
        CacheManager().update_font_cache()
        FileManager().remove_file("./data/db.lock")

        time.sleep(int(SystemService().find_system_info().refresh_rate) * 60 * 60)
