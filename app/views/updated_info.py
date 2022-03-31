from database.models.building import Building
from flask import Blueprint, render_template

bp_updated = Blueprint("updated", __name__, url_prefix="/updated")


@bp_updated.route("/list/")
def show_list():
    # 임시 지정
    buildings = Building.query.all()
    # 추후 order_by(Building.building_name.asc)

    return render_template(
        "updated_info/updated_info.html", updated_building_info=buildings
    )
