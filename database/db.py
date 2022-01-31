import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from models.base import Base

load_dotenv("../.env")

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'], echo=True)
Base.metadata.create_all(engine)
