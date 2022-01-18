from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main= Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def home():
    return render_template('/default/index.html')

@main.route('/main', methods=['GET'])
def index():
    test_data = 'test data array'
      # /main/index.html은 사실 /project_name/app/templates/main/index.html을 가리킵니다.
    return render_template('/main/index.html', test_data_html = test_data)
