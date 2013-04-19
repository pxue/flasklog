from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form, BooleanField, TextField, validators

db = SQLAlchemy()

class Post(db.Model):
    __tablename__ = 'posts'

    pid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)
    published = db.Column(db.Boolean)
    permalink = db.Column(db.Text)
    create_date = db.Column(db.DateTime)

    def __init__(self, title, author, published, permalink):
        self.title = title
        self.author = author
        self.published = published
        self.permalink = permalink
        self.create_date = datetime.now()

    def __repr__(self):
        return '<Post %r>' % self.title
    

class PostForm(Form):

    title = TextField('Title', [validators.Length(min=4, max=60)])
    author = TextField('Author', [validators.Length(min=4, max=25)])
    published = BooleanField('Publish')
    permalink = TextField('Permanent Link', [validators.Length(min=10, max=60)])
