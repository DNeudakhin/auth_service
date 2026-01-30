from config import env
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from testcontainers.core.wait_strategies import PortWaitStrategy
from testcontainers.postgres import PostgresContainer
from typing_extensions import AsyncGenerator, Generator

from config.settings import Settings
from infrastructure.persistence.manager import DBManager

HOST = 'localhost'
TEST_DB_PORT = 5433


@pytest.fixture(scope="session")
def postgres_container() -> Generator[PostgresContainer]:
    postgres = PostgresContainer(
        "postgres:16",
        username="test",
        password="test",
        dbname="test_db",
        driver="asyncpg",
    )
    postgres.with_bind_ports(5432, TEST_DB_PORT)
    postgres.start()
    yield postgres
    postgres.stop()

@pytest.fixture(scope="session")
def test_env(postgres_container: PostgresContainer) -> Settings:
    env
    return Settings(
        DB_NAME=postgres_container.dbname,
        DB_HOST=HOST,
        DB_PORT=TEST_DB_PORT,
        DB_USER=postgres_container.username,
        DB_PASSWORD=postgres_container.password,
    )

@pytest_asyncio.fixture(scope="session")
async def db_manager(test_env: Settings) -> AsyncGenerator[DBManager]:
    manager = DBManager(test_env)
    yield manager
    await manager.engine.dispose()
