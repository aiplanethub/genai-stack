import sqlalchemy as _sqlalchemy
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

from rest_api.core import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URI


# `pool_size` and `max_overflow` should be increased based on the number of traffic.
# If there are more concurrent requests even after overflowing, then they will be queued.
engine = _sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_recycle=600,  # seconds
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
