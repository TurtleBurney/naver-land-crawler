from flask import url_for
from werkzeug.utils import redirect

from app.views.blueprint import bp_main


@bp_main.route("/main")
def print_main():
    return "Main Page"


@bp_main.route("/")
def index():

    return redirect(url_for("building.show_list"))
    # url_for(블루프린트 이름(not 변수명).블루프린트에 등록된 함수명)
