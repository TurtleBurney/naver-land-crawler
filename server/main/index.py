# 메인페이지 전용 DIR
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
    test_data = 'posted_test_data'
    return render_template('/main/index.html', test_data_html = test_data)