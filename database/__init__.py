import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv(verbose=True)

engine = create_engine(os.getenv("SQLALCHEMY_DATABASE_URI"))

from sqlalchemy.orm import sessionmaker, scoped_session

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
