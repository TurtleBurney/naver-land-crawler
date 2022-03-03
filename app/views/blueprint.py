from flask import Blueprint

bp_main = Blueprint("main", __name__, url_prefix="/")

bp_issue = Blueprint("issue", __name__, url_prefix="/issue")
bp_updated = Blueprint("updated", __name__, url_prefix="/updated")
bp_building = Blueprint("building", __name__, url_prefix="/building")
