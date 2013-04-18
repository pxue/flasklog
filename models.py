from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'

    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    published = db.Column(db.Boolean)
    permalink = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

    def __init__(self):
        pass

    def __repr__(self):
        return '<Post %r>' % self.title
    

