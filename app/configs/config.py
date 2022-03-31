import os

from dotenv import load_dotenv

load_dotenv(verbose=True)

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
