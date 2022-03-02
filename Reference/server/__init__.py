# run.py에 있는 from app import app 을 통해 실행되는 모든 파일들을
# 전체적으로 초기화 및 실행을 위한 파일

from flask import Flask
from server.main.index import main as main

server = Flask(__name__)
server.register_blueprint(main)
