""" fontman desktop core

fontman client font management system main application script.

Created by Lahiru Pathirage @ Mooniak<lpsandaruwan@gmail.com> on 3/12/2016
"""

import socket
import threading

from flask import Flask

from blueprint import auth_blueprint
from blueprint import collections_blueprint
from blueprint import channels_blueprint
from blueprint import fontfaces_blueprint
from blueprint import fonts_blueprint
from blueprint import settings_blueprint
from blueprint import teams_blueprint
from blueprint import typecase_blueprint
from utility import FileManager
from utility import initialize
from utility import run_tasks


def run_flask_app():
    fms = Flask(__name__)

    fms.register_blueprint(auth_blueprint)
    fms.register_blueprint(collections_blueprint)
    fms.register_blueprint(channels_blueprint)
    fms.register_blueprint(fontfaces_blueprint)
    fms.register_blueprint(fonts_blueprint)
    fms.register_blueprint(settings_blueprint)
    fms.register_blueprint(teams_blueprint)
    fms.register_blueprint(typecase_blueprint)

    fms.run(host="0.0.0.0", threaded=True)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con = sock.connect_ex(('127.0.0.1', 5000))

    if con is not 0:
        if FileManager().is_file_exists("./data/fontman.db"):
            # threading.Thread(target=run_tasks).start()
            run_flask_app()

        else:
            initialize()
            threading.Thread(target=run_tasks).start()
            run_flask_app()
    else:
        print("Port is in use.")

if __name__ == '__main__':
    main()
