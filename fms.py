""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

from flask import Flask
from threading import Thread
import sys

from blueprint import about_blueprint
from blueprint import channel_blueprint
from blueprint import font_blueprint
from blueprint import operation_blueprint
from blueprint import preference_blueprint
from blueprint import profile_blueprint
from utility import CacheManager
from utility import ThreadRunner
from utility import initialize


def run_flask_app():
    fms = Flask(__name__)
    fms.register_blueprint(about_blueprint)
    fms.register_blueprint(channel_blueprint)
    fms.register_blueprint(font_blueprint)
    fms.register_blueprint(operation_blueprint)
    fms.register_blueprint(preference_blueprint)
    fms.register_blueprint(profile_blueprint)

    fms.run(host="0.0.0.0", threaded=True)


def run_threads():
    ThreadRunner().run()


def main(argv):
    for arg in argv:
        if "init" in arg:
            initialize()
            CacheManager().refresh_cache()

        if "start" in argv:
            Thread(target=run_threads).start()
            Thread(target=run_flask_app).start()


if __name__ == '__main__':
    # main(sys.argv[1:])
    # run_flask_app()
    initialize()
    CacheManager().refresh_cache()
