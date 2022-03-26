from dotenv import load_dotenv
from flask import session
from sqlalchemy import create_engine

load_dotenv(verbose=True)

engine = create_engine("SQLALCHEMY_DATABASE_URI")

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(engine)
session = Session()
