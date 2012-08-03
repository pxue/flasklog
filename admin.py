from flask import (Blueprint, request, render_template, redirect,
        url_for, abort)
from flask.views import MethodView
from flask.ext.wtf import (Form, TextField, Required, TextAreaField,
        SubmitField, PasswordField, ValidationError)
from auth import requires_auth
from models import Post
from utils import get_md_content, write_md_content

admin = Blueprint('admin', __name__, template_folder='templates')

class PostForm(Form):
    title = TextField("Title", validators=[Required()])
    permalink = TextField("Permalink", validators=[Required()])
    author = TextField("Author", default="Paul")
    content = TextAreaField("Content")
    submit = SubmitField("Save Changes")

class LoginForm(Form):
    
    username = TextField("Username")
    password = PasswordField("Password")
    submit = SubmitField("Login")

class ListView(MethodView):
    decorators = [requires_auth]
    cls = Post

    def get(self):
        posts = self.cls.PostsByDate()
        return render_template('admin/index.html', posts = posts)

class DetailView(MethodView):

    decorators = [requires_auth]

    def get_context(self, permalink=None):
        form_cls = PostForm()
        
        if permalink:
            post = Post.by_permalink[permalink].rows[0]
            if post is None: abort(404)

            if request.method == "POST":
                form = form_cls
            else:
                form_cls.content.data = get_md_content(permalink, False)
                form = form_cls
        else:
            post = Post()
            form = form_cls

        context={
            "post": post,
            "form": form,
            "create": permalink is None
        }

        return context

    def get(self, permalink):
        context = self.get_context(permalink)
        return render_template('admin/detail.html', **context)

    def post(self, permalink):
        context = self.get_context(permalink)
        form = context.get('form')

        if form.validate():
            post = context.get('post')
            form.populate_obj(post)

            write_md_content(post.permalink, form.content.data)

            return redirect(url_for('admin.index'))
        return render_template('admin/detail.html', **context)

admin.add_url_rule('/admin/', view_func=ListView.as_view('index'))
admin.add_url_rule('/admin/create', defaults={'permalink': None},
        view_func=DetailView.as_view('create'))
admin.add_url_rule('/admin/<permalink>', view_func=DetailView.as_view('edit'))
