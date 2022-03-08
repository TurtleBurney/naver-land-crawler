# sys path appending
import os
import sys

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../../')
)

sys.path.insert(0, ROOT_DIR)

# Migration
from alembic import context

config = context.config

_FLASK = "flask"
_ALEMBIC = "alembic"

migration_type = config.get_main_option("type", _ALEMBIC)

if migration_type == _FLASK:
    from flask import current_app
    
    url = current_app.config.get("SQLALCHEMY_DATABASE_URI", None)

    config.set_main_option("sqlalchemy.url", url)

    target_metadata = current_app.extension['migrate'].db.metadata

elif migration_type == _ALEMBIC:
    from database.testModels.base import Base
    
    assert "SQLALCHMEY_DATABASE_URI" in os.environ
    url = os.environ("SQLALCHEMY_DATABASE_URI")
    
    config.set_main_option("sqlalchemy.url", url)
    
    target_metadata = Base.metadata

else:
    raise Exception("Invalid Migration Type")

# Logging 
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # this callback is used to prevent an auto-migration from being generated
    # when there are no changes to the schema
    # reference: http://alembic.zzzcomputing.com/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if getattr(config.cmd_opts, "autogenerate", False):
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []
                print("Notting changes in scheman detected")      

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata,
            compare_type=True,
            process_revision_directives=process_revision_directives,            
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
