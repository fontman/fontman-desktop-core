""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

from flask import Flask

from utility import CacheManager
from utility import initialize
from utility import Operation

from blueprint import about_blueprint, channel_blueprint, font_blueprint, \
    operation_blueprint, preference_blueprint


def run_flask_app():
    fms = Flask(__name__)
    fms.register_blueprint(about_blueprint)
    fms.register_blueprint(channel_blueprint)
    fms.register_blueprint(font_blueprint)
    fms.register_blueprint(operation_blueprint)
    fms.register_blueprint(preference_blueprint)

    fms.run(debug=True, host="0.0.0.0", threaded=True)


def main():
    initialize()
    CacheManager().update_github_font_cache()
    # Operation().remove_font("post")


if __name__ == '__main__':
    # main()
    run_flask_app()
