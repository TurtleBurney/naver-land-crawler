from flask import Blueprint, render_template
from app.models.building import Building

bp_building = Blueprint('building', __name__, url_prefix='/building')

@bp_building.route('/')
def index():
    buildings = Building.query.all()
    # 추후 order_by(Building.building_name.asc)
    return render_template('building/building_list.html', building_list = buildings)

@bp_building.route('/detail/<int:building_id>/')
def detail(building_id):
    building = Building.query.get_or_404(building_id)
    return render_template('building/building_detail.html', building = building)