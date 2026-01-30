import pytest_asyncio
import pytest
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from infrastructure.persistence.manager import DBManager


@pytest.mark.asyncio
async def test_db_engine(db_manager: DBManager):
    assert isinstance(db_manager.engine, AsyncEngine)

    async with db_manager.engine.connect() as conn:
        result = await conn.execute(text("SELECT 1"))
        value = result.scalar_one_or_none()
        assert value and value == 1
        
    assert conn.closed

@pytest.mark.asyncio
async def test_session(db_manager: DBManager):
    async with db_manager.session_maker() as session:
        assert isinstance(session, AsyncSession)
         
        result = await session.execute(text("SELECT 1"))
        value = result.scalar_one_or_none()
        assert value and value == 1
