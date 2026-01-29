import uuid

from typing_extensions import Protocol

from domain.entity import User


class UserRepository(Protocol):
    async def get_user_by_email(self, email: str) -> User | None: ...

    async def create_user(self, entity: User) -> uuid.UUID: ...
