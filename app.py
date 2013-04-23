from flask import Flask, render_template
from views.frontend import frontend
from views.admin import backend
from models import db
from utils import filter_datetime, get_md_content
from auth import login_manager
import settings

app = Flask(__name__)
app.config.from_object(settings.Config)

# blueprint
app.register_blueprint(frontend, url_prefix="")
app.register_blueprint(backend)

# jinja filters
app.jinja_env.filters['datetime'] = filter_datetime
app.jinja_env.filters['parsemd'] = get_md_content

# sqlalchemy db instance
db.init_app(app)

# login manager
login_manager.setup_app(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")
