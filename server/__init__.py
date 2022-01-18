from flask import Flask

server = Flask(__name__)

from server.main.index import main as main
server.register_blueprint(main)