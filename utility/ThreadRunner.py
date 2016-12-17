""" Thread runner

Run actions in threads

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 10/12/2016
"""

import os, platform, re, time
from threading import Thread

from service import FontFileService, InstalledFontService, SystemService
from session import db_lock
from utility import CacheManager

# conditional imports for windows platform
if platform.system() in "Windows":
    import win32api
    import win32con
    import ctypes


class ThreadRunner:

    def __init__(self):
        self.__system = SystemService().find_system_info()
        self.__font_cache = self.__system.fontman_home + "temp"
        self.__platform = self.__system.platform

    def run(self):
        # refresh windows fonts cache
        if self.__platform in "Windows":
            Thread(target=self.refresh_installed_fonts_windows_fix).run()

        # schedule cache update
        Thread(target=self.refresh_cache).run()

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
            cache.update_font_cache()

    def refresh_installed_fonts_windows_fix(self):
        try:
            for font in InstalledFontService().find_all():
                for font_file in FontFileService().find_all_by_font_id(
                    font.font_id
                ):
                    file_path = os.path.join(
                        self.__font_cache,
                        font.font_id,
                        font_file.file_name
                    )

                    ctypes.windll.gdi32.AddFontResourceA(
                        file_path
                    )
        except:
            print("Install some fonts... :-)")

        # inform windows new fonts have been added
        win32api.SendMessage(win32con.HWND_BROADCAST, win32con.WM_FONTCHANGE)
