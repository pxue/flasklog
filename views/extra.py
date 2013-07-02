from flask import (Flask, render_template, Blueprint)

extra = Blueprint('extra', __name__, static_folder='static',
     template_folder='templates')

@extra.route('/extra/d41d8cd98f00b204e9800998ecf8427e')
def gotrans():
    return render_template('extra/gotrans.html')
