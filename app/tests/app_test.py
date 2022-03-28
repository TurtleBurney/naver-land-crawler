import pytest

from app.configs import testing as config
from app.source import create_app

TEST_CONFIG = {
    "TESTING": True,
}


@pytest.fixture(scope="session")
def app():
    app = create_app(TEST_CONFIG)
    return app


@pytest.fixture(scope="session")
def app_client(app):
    return app.test_client()
