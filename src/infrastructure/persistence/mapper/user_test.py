import uuid

import pytest
from faker import Faker

from domain import entity as entities
from infrastructure.persistence import model as models
from infrastructure.persistence.mapper import UserMapper

faker = Faker()


@pytest.mark.parametrize(
    (
        "id",
        "username",
        "email",
        "password",
    ),
    [(faker.uuid4(), faker.user_name(), faker.email(), faker.password())],
)
def test_to_entity_roundtrip(
    id: uuid.UUID, username: str, email: str, password: str
):
    original_model = models.User(
        id=id,
        user_name=username,
        email=email,
        password=password,
    )

    entity = UserMapper.to_domain(original_model)
    mapped_model = UserMapper.to_orm(entity)

    assert mapped_model.id == original_model.id
    assert mapped_model.user_name == original_model.user_name
    assert mapped_model.email == original_model.email
    assert mapped_model.password == original_model.password


@pytest.mark.parametrize(
    (
        "id",
        "username",
        "email",
        "password",
    ),
    [(faker.uuid4(), faker.user_name(), faker.email(), faker.password())],
)
def test_to_model_roundtrip(
    id: uuid.UUID, username: str, email: str, password: str
):
    original_entity = entities.User(
        id=id, user_name=username, email=email, hashed_password=password
    )

    model = UserMapper.to_orm(original_entity)
    mapped_entity = UserMapper.to_domain(model)

    assert original_entity.id == mapped_entity.id
    assert original_entity.user_name == mapped_entity.user_name
    assert original_entity.email == mapped_entity.email
    assert original_entity.password == mapped_entity.password


@pytest.mark.parametrize(
    (
        "id",
        "username",
        "email",
        "password",
    ),
    [(faker.uuid4(), faker.user_name(), faker.email(), faker.password())],
)
def test_to_entity_maps(
    id: uuid.UUID, username: str, email: str, password: str
):
    model = models.User(
        id=id,
        user_name=username,
        email=email,
        password=password,
    )

    entity = UserMapper.to_domain(model)

    assert entity.id == id
    assert entity.user_name == username
    assert entity.email == email
    assert entity.password == password


@pytest.mark.parametrize(
    (
        "id",
        "username",
        "email",
        "password",
    ),
    [(faker.uuid4(), faker.user_name(), faker.email(), faker.password())],
)
def test_to_model_maps(
    id: uuid.UUID, username: str, email: str, password: str
):
    entity = entities.User(
        id=id,
        user_name=username,
        email=email,
        hashed_password=password,
    )

    model = UserMapper.to_orm(entity)

    assert model.id == id
    assert model.user_name == username
    assert model.email == email
    assert model.password == password
