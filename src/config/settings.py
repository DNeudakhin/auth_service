from pathlib import Path

from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    DEBUG: bool = True
    SECRET_KEY: str = "secret"

    DB_NAME: str = "postgres"
    DB_HOST: str = "0.0.0.0"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_PORT: int = 5432

    class Config:
        env_file = BASE_DIR / ".env"


env = Settings()
