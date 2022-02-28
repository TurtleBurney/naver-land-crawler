from flask import Blueprint, render_template
from app.models.building_basic import BuildingBasic

bp_building = Blueprint('building', __name__, url_prefix='/building')

@bp_building.route('/list/')
def show_list():
    buildings = BuildingBasic.query.all()
    # 추후 order_by(Building.building_name.asc)
    return render_template('building/building_list.html', building_list = buildings)

@bp_building.route('/detail/<int:building_id>/')
def detail(building_id):
    building = BuildingBasic.query.get_or_404(building_id)
    return render_template('building/building_detail.html', building = building)