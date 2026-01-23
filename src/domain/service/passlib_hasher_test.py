import pytest
from faker import Faker
from typing_extensions import Any

from domain.service.passlib_hasher import PasslibHasher

faker = Faker()


@pytest.fixture(scope="module")
def passlib_hasher() -> PasslibHasher:
    return PasslibHasher("secret")


@pytest.mark.parametrize(
    "string", [faker.password(), faker.pystr(), faker.email()]
)
def test_hashing_string(string: str, passlib_hasher: PasslibHasher):
    hashed_string = passlib_hasher.hash(string)

    assert string != hashed_string


@pytest.mark.parametrize(
    "value", [faker.boolean(), faker.random_int(), faker.pyfloat(), [], ()]
)
def test_error_hashing_string(value: Any, passlib_hasher: PasslibHasher):
    with pytest.raises(ValueError):
        passlib_hasher.hash(value)


@pytest.mark.parametrize(
    "string", [faker.password(), faker.pystr(), faker.email()]
)
def test_compare_hashing_string(string: str, passlib_hasher: PasslibHasher):
    hashed_string = passlib_hasher.hash(string)

    assert string != hashed_string
    assert passlib_hasher.compare(string, hashed_string)

@pytest.mark.parametrize('hashed_string', [faker.pystr()])
@pytest.mark.parametrize(
    "value", [faker.boolean(), faker.random_int(), faker.pyfloat(), [], ()]
)
def test_error_comapre_hashing_string(hashed_string, value: Any, passlib_hasher: PasslibHasher):
    with pytest.raises(ValueError):
        passlib_hasher.compare(value, hashed_string)