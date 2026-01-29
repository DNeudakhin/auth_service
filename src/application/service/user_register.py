import uuid

from application import dtos, interfaces
from domain.entity import User


class UserRegisterService:
    __slots__ = ("_repo", "_hasher")

    def __init__(
        self, repo: interfaces.UserRepository, hasher: interfaces.Hasher
    ) -> None:
        self._repo: interfaces.UserRepository = repo
        self._hasher: interfaces.Hasher = hasher

    async def execute(self, data: dtos.RegisterUser) -> uuid.UUID:
        hashed_password = self._hasher.hash(data.password)

        user = User(
            user_name=data.user_name,
            email=data.email,
            hashed_password=hashed_password,
        )

        return await self._repo.create_user(user)
