""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

from flask import Flask
import sys

from blueprint import about_blueprint, channel_blueprint, font_blueprint, \
    operation_blueprint, preference_blueprint

from utility import CacheManager, initialize, ThreadRunner


def run_flask_app():
    fms = Flask(__name__)
    fms.register_blueprint(about_blueprint)
    fms.register_blueprint(channel_blueprint)
    fms.register_blueprint(font_blueprint)
    fms.register_blueprint(operation_blueprint)
    fms.register_blueprint(preference_blueprint)

    fms.run(debug=True, host="0.0.0.0", threaded=True)


def run_threads():
    ThreadRunner("cache_refresh").run()

def main(argv):
    for arg in argv:
        print(arg)

        if "init" in arg:
            initialize()
            CacheManager().update_github_font_cache()

        if "start" in argv:
            run_threads()
            run_flask_app()


if __name__ == '__main__':
    main(sys.argv[1:])
    # run_flask_app()
    # initialize()
    # CacheManager().update_github_font_cache()
