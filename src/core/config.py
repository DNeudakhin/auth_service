from pathlib import Path
from pygments.lexer import default
from dataclasses import dataclass
from decouple import Config, RepositoryEnv

BASE_DIR = Path(__file__).resolve().parent.parent
config = Config(RepositoryEnv(BASE_DIR / '.env'))

@dataclass(slots=True, frozen=True)
class Config:
    db_name: str = config.get('DB_NAME', default='')
    db_host: str = config.get('DB_HOST', default='')
    db_user: str = config.get('DB_USER', default='')
    db_password: str = config.get('DB_PASSWORD', default='')
    db_port: int = config.get('DB_PORT', default=0, cast=int)

config = Config()