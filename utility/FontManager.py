""" Font management tools

Access system fonts library and manipulate.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 28/12/2016
"""

import fontconfig
import platform


class FontManager:

    def get_system_font_list(self):
        if platform.system() in "Windows":
            return
        return fontconfig.query()

    def find_by_font_family(self, font_family):
        return fontconfig.query(family=font_family)

