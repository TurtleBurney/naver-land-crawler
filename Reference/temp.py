import sqlalchemy
import os
from models.base import Base

def main():
    engine = sqlalchemy.create_engine(os.environ["SQLALCHEMY_DATABASE_URI"], echo=True)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    main()
