from database.models.building import Building
from flask import Blueprint, render_template

bp_building = Blueprint("building", __name__, url_prefix="/building")


@bp_building.route("/list/")
def show_list():
    # TODO : controller 만들어 db에서 정보 받아오기
    buildings = None
    # buildings = Building.query.all()
    # 추후 order_by(Building.building_name.asc)
    return render_template("building/building_list.html", building_list=buildings)


@bp_building.route("/detail/<int:building_id>/")
def show_detail(building_id):
    building = Building.query.get_or_404(building_id)

    return render_template("building/building_detail.html", building=building)
