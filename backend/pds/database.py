from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from pds.settings import get_settings

Base = declarative_base()


def get_session() -> Session:
    settings = get_settings().database

    engine = create_engine(
        settings.uri,
        echo=settings.echo,
        pool_pre_ping=settings.pool_pre_ping,
        pool_size=settings.pool_size,
        max_overflow=settings.pool_max_overflow,
    )
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
