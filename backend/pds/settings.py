from functools import lru_cache
from pprint import pprint
from typing import Any

from pydantic import BaseSettings, PostgresDsn, validator, Field

ENV_FILE = ".env"


class Database(BaseSettings):
    class Config:
        env_prefix = "database_"
        env_file = ENV_FILE

    pool_pre_ping: bool = True
    pool_size: int = 10
    pool_max_overflow: int = 0
    echo: bool = False
    encryption_keys: list[str] = []

    host: str = "localhost"
    user: str = "postgres"
    port: str = "5432"
    password: str = "7bc3e5fb8e334bebbaee50f05658dcb7"
    name: str = "wds-test"
    uri: PostgresDsn = ""

    @validator("uri", pre=True)
    def assemble_db_connection(
        cls,
        v: str | None,
        values: dict[str, Any],
    ) -> Any:
        if v:
            return v
        else:
            return PostgresDsn.build(
                scheme="postgresql",
                user=values.get("user"),
                port=values.get("port"),
                password=values.get("password"),
                host=values.get("host"),
                path=f"/{values.get('name') or ''}",
            )


class Settings(BaseSettings):
    class Config:
        env_file = ENV_FILE

    debug: bool = False
    testing: bool = False
    env: str = "dev"
    database: Database = Field(default_factory=Database)
    server_name: str = "localhost"

    acces_token_expire_minutes: int = 30
    algorithm: str = "HS256"
    secret_key: str = "your-secret-key"


@lru_cache()
def get_settings() -> Settings:
    settings = Settings()
    return settings


def show():
    settings = Settings()
    pprint(settings.dict())
