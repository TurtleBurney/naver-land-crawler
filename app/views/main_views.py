from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main')
def print_main():
    return 'Main Page'

@bp.route('/')
def index():
    return 'Hello, Flask'