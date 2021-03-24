import re
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base, declared_attr

Model = declarative_base()


class Base:
    @declared_attr
    def __tablename__(cls):
        s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", cls.__name__)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()

    def __repr__(self):
        return f"<{self.__class__.__name__}>"


class BaseModel(Base):
    pass
    # created_datetime = sa.Column(
    #     sa.DateTime, nullable=False, index=True, default=datetime.now
    # )
    # modified_datetime = sa.Column(sa.DateTime, onupdate=datetime.now)
# launcher 실행을 위해 임시로 주석처리 시행