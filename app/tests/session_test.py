import pytest

from flask import g


@pytest.fixture(scope="function")
def session(db):
    session = db["session"]()
    g.db = session

    yield session

    session.rollback()
    session.close()
