import datetime
from flask.ext.couchdb import Document, TextField, BooleanField, \
        DateTimeField, ViewField
from flask import url_for

class Post(Document):

    author = TextField()
    title = TextField()
    published = BooleanField(default=True)
    permalink = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    PostsByDate = ViewField( 'Post', '''\
    function(doc){
        if(doc.model_type === 'Post' && doc.date){
            emit(doc.date, doc)
        }
    }''', descending=True)

    by_permalink = ViewField('Post', '''\
    function(doc){
        if(doc.model_type === 'Post'){
            emit(doc.permalink, doc)
        }
    }
    ''')

    def get_permalink(self):
        return url_for('posts', kwargs={"permalink": self.permalink})

    def __unicode__(self):
        return self.title
