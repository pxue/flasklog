from flask import (Flask, render_template, Blueprint, request,
        flash, redirect, url_for)
from flask.ext.login import login_user, logout_user, login_required
from utils import get_md_content
from models import Post
from auth import USER_NAMES, hash_pass

frontend = Blueprint('frontend', __name__, static_folder='static', template_folder='templates')

@frontend.route('/')
@frontend.route('/<int:page>')
def index(page=1):
    posts = Post.query.filter_by(published='t').order_by(Post.create_date.desc()).paginate(page, 1, False)
    return render_template("index.html", posts=posts)

@frontend.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST" and "username" in request.form:
        username = request.form["username"]
        if username in USER_NAMES:
            password = hash_pass(request.form["password"],
                    USER_NAMES.get(username).salt)
            if password == USER_NAMES[username].password:
                remember = request.form.get("remember", "no") == "yes"
                if login_user(USER_NAMES[username], remember=remember):
                    flash("You're logged in!")
                    return redirect(request.args.get("next") or
                            url_for("admin.admin"))
            else:
                flash("Something is wrong")
        else:
            flash("Invalid username")
    return render_template("login.html")

@frontend.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("Logged out")
    return redirect(url_for("frontend.index"))

