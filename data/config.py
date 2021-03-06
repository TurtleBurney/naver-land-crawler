import os
import typing
from cryptography.fernet import Fernet


class MissingConfig(KeyError):
    pass


SCHEMA = {
    #: SQLAlchemy URI
    "DATABASE_URI": str,
}


def load_config():
    cipher_suite = Fernet(os.environ["KEY"].encode())
    config = {}
    prefix = ""
    schema = SCHEMA

    for name, field in schema.items():
        prefixed = prefix + name
        if prefixed.upper() not in os.environ:
            raise MissingConfig

        config[name] = cipher_suite.encrypt(f"{os.environ[prefixed.upper()]}".encode())
    return config
