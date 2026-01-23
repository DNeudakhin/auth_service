import uuid

import pytest
from faker import Faker

from core.service.hasher import FakeHasher
from domain.entity import User

faker = Faker()


@pytest.mark.parametrize(
    "user_name,email,password,hashed_password",
    [
        (faker.user_name(), faker.email(), faker.password(), faker.password()),
        (faker.user_name(), faker.email(), faker.password(), faker.password()),
        (faker.user_name(), faker.email(), faker.password(), faker.password()),
    ],
)
def test_create_new_user(
    user_name: str, email: str, password: str, hashed_password: str
) -> None:
    hasher = FakeHasher(hashed_password)
    user = User.create(
        user_name=user_name, email=email, password=password, hasher=hasher
    )

    assert isinstance(user, User)
    assert user.id is not None and isinstance(user.id, uuid.UUID)
    assert user.user_name == user_name
    assert user.email == email
    assert user.password != password, (
        "User password must be different after hash."
        f"plain={password}, hashed={user.password}"
    )


@pytest.mark.parametrize(
    "id,user_name,email,hashed_password",
    [
        (uuid.uuid4(), faker.user_name(), faker.email(), faker.password()),
        (uuid.uuid4(), faker.user_name(), faker.email(), faker.password()),
        (uuid.uuid4(), faker.user_name(), faker.email(), faker.password()),
    ],
)
def test_load_user_from_persistence_storage(
    id: uuid.UUID, user_name: str, email: str, hashed_password: str
) -> None:
    user = User.from_persistence_storage(
        id=id,
        user_name=user_name,
        email=email,
        hashed_password=hashed_password,
    )

    assert isinstance(user, User)
    assert (
        user.id is not None
        and isinstance(user.id, uuid.UUID)
        and user.id == id
    )
    assert user.user_name == user_name
    assert user.email == email
    assert user.password == hashed_password
