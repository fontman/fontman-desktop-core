""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""
from utility import CacheManager
from utility import initialize


def main():
    initialize()
    CacheManager().update_github_font_cache()


if __name__ == '__main__':
    main()
