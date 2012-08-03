import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.actions import Manager
from flasklog import app

manager = Manager(app, default_server_actions=True)

if __name__ == "__main__":
    manager.run()
