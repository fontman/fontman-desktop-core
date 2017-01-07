""" fms

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

from flask import Flask

from utility import initialize


def run_flask_app():
    fms = Flask(__name__)

    fms.run(host="0.0.0.0", threaded=True)


if __name__ == '__main__':
    # run_flask_app()
    initialize()
