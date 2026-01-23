import uuid

from typing_extensions import Self

from core.entity import Entity
from core.exceptions import EmptyStringError
from core.service import AbstractHasher


class User(Entity):
    __slots__ = ("user_name", "email", "password")

    def __init__(
        self,
        user_name: str,
        email: str,
        hashed_password: str | None = None,
        id: uuid.UUID | None = None,
    ) -> None:
        super().__init__(id)
        self.user_name: str = user_name
        self.email: str = email
        self.password: str | None = hashed_password

    @classmethod
    def create(
        cls,
        user_name: str,
        email: str,
        password: str,
        hasher: AbstractHasher,
    ) -> Self:
        if not password:
            raise EmptyStringError("Password string can't be empty")
        hashed_password = hasher.hash(password)
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
