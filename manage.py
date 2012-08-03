import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#from flask.ext.script import Manager, Server
from flask.ext.actions import Manager
from flasklog import app

manager = Manager(app, default_server_actions=True)

#manager.add_command('runserver', Server(
    #use_debugger = True,
    #use_reloader = True,
    #host = '0.0.0.0',)
#)

if __name__ == "__main__":
    manager.run()
