import uuid

from typing_extensions import Self

from core.entity import Entity
from core.hasher import AbstractHasher


class User(Entity):
    __slots__ = ("user_name", "email", "_password")

    user_name: str
    email: str
    _password: str

    def __init__(
        self,
        user_name: str,
        email: str,
        hashed_password: str,
        id: uuid.UUID | None = None,
    ) -> None:
        super().__init__(id)
        self.user_name = user_name
        self.email = email
        self._password = hashed_password

    @property
    def password(self) -> str:
        return self._password

    @classmethod
    def create(
        cls,
        user_name: str,
        email: str,
        raw_password: str,
        hasher: AbstractHasher,
    ) -> Self:
        hashed_password = hasher.hash(raw_password)
        return cls(
            user_name=user_name, email=email, hashed_password=hashed_password
        )

    @classmethod
    def from_persistence_storage(
        cls,
        id: uuid.UUID,
        user_name: str,
        email: str,
        hashed_password: str,
    ) -> Self:
        return cls(
            id=id,
            user_name=user_name,
            email=email,
            hashed_password=hashed_password,
        )

    def set_password(self, raw_password: str, hasher: AbstractHasher) -> Self:
        self._password = hasher.hash(raw_password)
        return self

    def compare_password(
        self, raw_password: str, hasher: AbstractHasher
    ) -> bool:
        return hasher.compare(raw_password, self._password)
