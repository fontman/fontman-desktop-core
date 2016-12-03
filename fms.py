""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

from flask import Flask

from utility import CacheManager
from utility import initialize

from blueprint import font_blueprint


def run_flask_app():
    fms = Flask(__name__)
    fms.register_blueprint(font_blueprint)

    fms.run(host="0.0.0.0")


def main():
    initialize()
    CacheManager().update_github_font_cache()


if __name__ == '__main__':
    run_flask_app()
