import re
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
# ORM 객체
Model = declarative_base()


class Base:
    @declared_attr
    # 상속을 활용해 tablename의 포맷 지정
    def __tablename__(cls):
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", cls.__name__)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class BaseModel(Base):
    created_datetime = Column(
        DateTime, nullable=False, index=True, default=datetime.now
    )
    modified_datetime = Column(DateTime, onupdate=datetime.now)
