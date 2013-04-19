from flask import (Flask, render_template, Blueprint, request,
        flash, redirect, url_for)
from flask.ext.login import login_required
from utils import get_md_content
from models import Post, PostForm, db

backend = Blueprint('backend', __name__, static_folder='static',
        template_folder='templates')

@backend.route('/admin', methods=['GET', 'POST', 'PUT'])
@login_required
def backend_list():
    
    posts = Post.query.order_by(Post.create_date.desc())
    return render_template('backend/index.html', posts=posts)

@backend.route('/admin/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post(form.title.data, form.author.data,
                form.published.data, form.permalink.data)
        db.session.add(post)
        try:
            db.session.commit()
            flash("Post added successfully!")
        except Exception, e:
            flash("%s", e)

        return redirect(url_for("backend.backend_list"))

    return render_template('backend/create.html', form=form)
