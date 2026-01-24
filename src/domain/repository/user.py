import abc
import uuid

from domain.entity import User


class AbstractUserRepository(abc.ABC):
    @abc.abstractmethod
    async def get_user_by_email(self, email: str) -> User | None: ...

    @abc.abstractmethod
    async def create_user(self, entity: User) -> uuid.UUID: ...


class FakerUserRepository(AbstractUserRepository):
    __slots__ = "_storage"

    def __init__(self) -> None:
        self._storage: dict[str, User] = {}

    async def get_user_by_email(self, email: str) -> User | None:
        return self._storage.get(email)

    async def create_user(self, entity: User) -> uuid.UUID:
        self._storage[entity.email] = entity
        return entity.id
