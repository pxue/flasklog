import os, codecs
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form, BooleanField, TextField, TextAreaField, validators

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

    @property
    def content(self):
        path = "%s/posts/%s.md" % (os.getcwd(), self.permalink)
        return codecs.open(path, mode="r", encoding="utf-8").read()

    def post_form(self, request_form):
        form = PostForm(request_form)
        form.title.data = self.title
        form.author.data = self.author
        form.published.data = self.published
        form.permalink.data = self.permalink
        form.content.data = self.content
        return form

    def __repr__(self):
        return '<Post %r>' % self.title
    

class PostForm(Form):

    title = TextField('Title', [validators.Length(min=4, max=60)])
    author = TextField('Author', [validators.Length(min=4, max=25)])
    published = BooleanField('Publish')
    permalink = TextField('Permanent Link', [validators.Length(min=10, max=60)])
    content = TextAreaField('Content')
