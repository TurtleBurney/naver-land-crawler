from flask import render_template

from app.views.blueprint import bp_updated

from database.models.building_basic import BuildingBasic


@bp_updated.route("/list/")
def show_list():
    # 임시 지정
    buildings = BuildingBasic.query.all()
    # 추후 order_by(Building.building_name.asc)
    return render_template(
        "updated_info/updated_info.html", updated_building_info=buildings
    )
