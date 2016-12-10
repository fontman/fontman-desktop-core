""" Thread runner

Run actions in threads

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 10/12/2016
"""

import re, threading, time

from service import SystemService
from session import db_lock
from utility import CacheManager


class ThreadRunner(threading.Thread):

    def __init__(self, thread_id):
        threading.Thread.__init__(self)

    def run(self):
        print("Starting thread, System update")
        self.refresh_cache()
        print("Exiting thread, System update")

    def refresh_cache(self):
        refresh_rate = int(
            re.search(
                r'\d+', SystemService().find_system_info().refresh_rate
            ).group()
        )

        cache = CacheManager()

        while True:
            time.sleep(refresh_rate * 60 * 60)

            while db_lock:
                time.sleep(1)

            # update cache
            cache.update_github_font_cache()
