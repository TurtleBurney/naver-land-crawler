import structlog
import sqlalchemy as sa
from sqlalchemy import orm

logger = structlog.get_logger()


class DBClient(object):
    """
    DATABASE

    """

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.session_factory = self.create_session_factory()

    def create_session_factory(self):
        """
        초기 db 세션을 만듭니다.
        """

        db_engine = sa.create_engine(self.config["DATABASE_URI"])
        session_factory = orm.sessionmaker(bind=db_engine)
        return session_factory
