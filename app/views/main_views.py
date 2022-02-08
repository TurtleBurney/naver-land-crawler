from flask import Blueprint, render_template
from app.models.building import Building
from app.models.household import Household
# 경로가 왜 app부터 시작할까..??

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/main')
def print_main():
    return 'Main Page'

@bp.route('/')
def index():
    buildings = Building.query.all()
    # 추후 order_by(Building.building_name.asc)
    return render_template('building/building_list.html', building_list = buildings)

@bp.route('/detail/<int:building_id>/')
def detail(building_id):
    building = Building.query.get_or_404(building_id)
    return render_template('building/building_detail.html', building = building)