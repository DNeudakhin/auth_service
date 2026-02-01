import uuid

import pytest
import pytest_asyncio
from faker import Faker

from domain import entity
from infrastructure.persistence import model
from infrastructure.persistence.manager import DBManager
from infrastructure.repository import SqlAlchemyUserRepository

faker = Faker()


@pytest_asyncio.fixture
async def user_repo(db_manager: DBManager, recreate_tables):
    return SqlAlchemyUserRepository(db_manager)


@pytest.fixture
def random_user() -> entity.User:
    return entity.User(
        id=uuid.uuid4(),
        user_name=faker.user_name(),
        hashed_password=faker.password(),
        email=faker.email(),
    )


@pytest.mark.asyncio
async def test_get_exist_user(
    random_user: entity.User,
    db_manager: DBManager,
    user_repo: SqlAlchemyUserRepository,
):
    async with db_manager.session_maker() as session:
        session.add(
            model.User(
                id=random_user.id,
                user_name=random_user.user_name,
                email=random_user.email,
                password=random_user.password,
            )
        )
        await session.commit()

    user_by_email = await user_repo.get_user_by_email(random_user.email)
    user_by_uuid = await user_repo.get_user_by_id(random_user.id)

    assert user_by_email is not None and isinstance(user_by_email, entity.User)
    assert user_by_uuid is not None and isinstance(user_by_uuid, entity.User)


@pytest.mark.asyncio
async def test_get_not_exist_user(user_repo: SqlAlchemyUserRepository):
    user_by_email = await user_repo.get_user_by_email(faker.email())
    user_by_uuid = await user_repo.get_user_by_id(uuid.uuid4())

    assert user_by_email is None
    assert user_by_uuid is None


@pytest.mark.asyncio
async def test_create_user(
    random_user: entity.User,
    user_repo: SqlAlchemyUserRepository,
):
    id = await user_repo.create_user(random_user)
    assert isinstance(id, uuid.UUID)

    created_user = await user_repo.get_user_by_id(id)
    assert created_user and isinstance(created_user, entity.User)
    assert created_user.email == random_user.email
    assert created_user.user_name == random_user.user_name
    assert created_user.password == random_user.password
