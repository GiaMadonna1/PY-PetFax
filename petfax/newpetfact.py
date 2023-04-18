from flask import (Blueprint, render_template)

# the name of the blueprint, the location, and the URL prefix
bp = Blueprint('fact', __name__, url_prefix="/facts")

@bp.route('/facts/new')
def new():
    return render_template('new.html')