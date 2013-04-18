from flask import (Flask, render_template, Blueprint, request,
        flash, redirect, url_for)
from flask.ext.login import login_required
from utils import get_md_content
from models import Post

backend = Blueprint('admin', __name__, static_folder='static',
        template_folder='templates')

@backend.route('/admin', methods=['GET', 'POST', 'PUT'])
@login_required
def admin():
    
    posts = Post.query.order_by(Post.create_date.desc())
    return render_template('admin/index.html', posts=posts)
