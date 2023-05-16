import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from starlette.testclient import TestClient

from pds.database import Base, get_session
from pds.settings import get_settings
from server import app_maker


@pytest.fixture(scope="session", autouse=True)
def settings():
    settings = get_settings()
    settings.debug = True
    settings.testing = True

    return settings


@pytest.fixture(scope="session")
def engine(settings):
    settings = get_settings().database

    engine = create_engine(
        settings.uri,
        echo=settings.echo,
        pool_pre_ping=settings.pool_pre_ping,
        pool_size=settings.pool_size,
        max_overflow=settings.pool_max_overflow,
    )

    yield engine
    engine.dispose()


@pytest.fixture(scope="session")
def engine(settings):
    settings = get_settings().database

    engine = create_engine(
        settings.uri,
        echo=settings.echo,
        pool_pre_ping=settings.pool_pre_ping,
        pool_size=settings.pool_size,
        max_overflow=settings.pool_max_overflow,
    )

    yield engine


@pytest.fixture(scope="function")
def session(engine, settings):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    engine.echo = settings.database.echo

    Base.metadata.drop_all(bind=engine)

    try:
        Base.metadata.create_all(bind=engine)
        yield db
    finally:
        db.rollback()
        engine.echo = False
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def app(
    session,
):
    app = app_maker()
    app.dependency_overrides[get_session] = lambda: session
    return app


@pytest.fixture
def client(app):
    return TestClient(app=app)
