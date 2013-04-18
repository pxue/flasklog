import hashlib
from flask.ext.login import LoginManager, UserMixin
from settings import Config

login_manager = LoginManager()
login_manager.login_view = "frontend.login"
login_manager.login_message = u"Please log in to access this page."

@login_manager.user_loader
def load_user(username):
    return USER_NAMES.get(str(username))

def hash_pass(password, salt):
    salted_password = password + salt
    return hashlib.sha256(salted_password).hexdigest()

class User(UserMixin):
    def __init__(self, username, password, salt, active=True):
        self.username = username 
        self.password = password
        self.salt = salt
        self.active = active

    def get_id(self):
        return self.username

USER_NAMES = dict((v[0], User(*v)) for v in Config.ADMIN.itervalues())
