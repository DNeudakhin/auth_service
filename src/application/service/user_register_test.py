import pytest
from faker import Faker

from application.dtos.commands.auth import RegisterUserComand
from application.service.user_register import UserRegisterService
from core.service import FakeHasher
from domain.entity import User
from domain.repository.user import FakerUserRepository


@pytest.fixture(scope="function")
def fake_repo() -> FakerUserRepository:
    return FakerUserRepository()


@pytest.fixture(scope="function")
def fake_hasher(faker: Faker) -> FakeHasher:
    return FakeHasher(faker.password())


async def test_user_register_service(
    fake_repo: FakerUserRepository, fake_hasher: FakeHasher, faker: Faker
):
    command = RegisterUserComand(
        user_name=faker.user_name(),
        email=faker.email(),
        password=faker.password(),
    )

    serivce = UserRegisterService(repo=fake_repo, hasher=fake_hasher)

    id = await serivce.execute(command)

    entity = await fake_repo.get_user_by_email(command.email)

    assert isinstance(entity, User) and entity is not None
    assert entity.id == id
    assert entity.email == command.email
    assert entity.user_name == command.user_name
    assert entity.password != command.password
