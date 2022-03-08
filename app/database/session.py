from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.configs import config

def create_session():
    engine = create_engine(config['SQLALCHEMY_DATABASE_URI'], echo=True)   
    session = sessionmaker(bind=engine)

    return session
