import uuid
from unittest.mock import AsyncMock, Mock

import pytest
from faker import Faker

from application.dto import RegisterUser
from application.service import UserRegisterService

faker = Faker()


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("user_name", "email", "password", "hashed_password"),
    [(faker.user_name(), faker.email(), faker.password(), faker.password())],
)
async def test_user_register_service(
    user_name: str, email: str, password: str, hashed_password: str
):
    hasher = Mock()
    hasher.hash.return_value = hashed_password

    repo = AsyncMock()
    generated_id = uuid.uuid4()
    repo.create_user.return_value = generated_id

    data = RegisterUser(
        user_name=user_name,
        email=email,
        password=password,
    )

    serivce = UserRegisterService(repo=repo, hasher=hasher)

    id = await serivce.register(data)

    assert isinstance(id, uuid.UUID)
    assert generated_id == id

    repo.create_user.assert_awaited_once()
    hasher.hash.assert_called_once_with(password)
