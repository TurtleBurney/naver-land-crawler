from flask import Blueprint, url_for
from werkzeug.utils import redirect
from app.models.building import Building
from app.models.household import Household
# 경로가 왜 app부터 시작할까..??

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main')
def print_main():
    return 'Main Page'

@bp.route('/')
def index():
    return redirect(url_for('building.show_list'))
    # url_for(블루프린트 이름(not 변수명).블루프린트에 등록된 함수명)