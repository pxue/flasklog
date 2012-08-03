from flask import Blueprint, request, redirect, render_template, url_for, \
        abort
from flask.ext.couchdb import paginate
from flask.views import MethodView
from models import Post
from settings import OFFLINE
from utils import get_md_content

posts = Blueprint('posts', __name__, template_folder='templates')

class ListView(MethodView):
    
    def get(self):
        page = paginate(Post.PostsByDate(), 8, request.args.get('start'))
        return render_template('index.html', page=page, offline = OFFLINE)

class DetailedView(MethodView):

    def get(self, permalink):
        content = get_md_content(permalink)
        if content is None:
            abort(404)
        return render_template('post.html', content=content)

# register the urls
posts.add_url_rule('/', view_func=ListView.as_view('index'))
posts.add_url_rule('/posts/<permalink>/', view_func=DetailedView.as_view('detail'))
