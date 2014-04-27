from flask import (Flask, render_template, Blueprint)

extra = Blueprint('extra', __name__, static_folder='static',
     template_folder='templates')

@extra.route('/extra/d41d8cd98f00b204e9800998ecf8427e')
def gotrans():
    return render_template('extra/gotrans.html')

@extra.route('/extra/802623db0ffcef9d9fd4f297ad23dcca/<type>')
def coffee_by_day(type):
    if type == "day":
        return render_template('extra/coffee_by_wkday.html')
    else:
        return render_template('extra/coffee_by_shop.html')
