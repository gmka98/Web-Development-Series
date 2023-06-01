from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from pds.settings import get_settings
db_url = 'postgresql://postgres:7bc3e5fb8e334bebbaee50f05658dcb7@localhost:5432/wds_test'

Base = declarative_base()

def get_session() -> Session:
    settings = get_settings().database

    engine = create_engine(db_url)
    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
