import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic.command import upgrade as alembic_upgrade
from alembic.config import Config as alembic_Config

from app.configs import testing as config


@pytest.fixture(scope='session')
def db():
    engine = create_engine(config['TEST_DB_URL'], echo=True)
    session = sessionmaker(bind=engine)
    
    _db = {
        'engine': engine,
        'session': session
    }
    
    alembic_config = alembic_Config(config['ALEMBIC_INI'])
    alembic_config.set_main_option('sqlalchemy.url', config['TEST_DB_URL'])
    alembic_upgrade(alembic_config, 'head')
    
    yield _db
    
    engine.dispose()