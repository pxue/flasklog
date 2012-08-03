from flask import Flask
import flaskext.couchdb
from flask.ext.couchdb import CouchDBManager
from settings import *
from models import *

app = Flask(__name__)
app.debug = True
app.config['COUCHDB_SERVER'] = settings.COUCHDB_SERVER
app.config['COUCHDB_DATABASE'] = settings.COUCHDB_DATABASE
app.config['SECRET_KEY'] = settings.SECRET_KEY

db = CouchDBManager()
db.add_document(Post)
db.setup(app)

def register_blueprints(app):
    from views import posts
    from admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
