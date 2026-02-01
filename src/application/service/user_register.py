import uuid

from application import dto, interface
from domain.entity import User


class UserRegisterService:
    __slots__ = ("_repo", "_hasher")

    def __init__(
        self, repo: interface.UserRepository, hasher: interface.Hasher
    ) -> None:
        self._repo: interface.UserRepository = repo
        self._hasher: interface.Hasher = hasher

    async def register(self, data: dto.RegisterUser) -> uuid.UUID:
        hashed_password = self._hasher.hash(data.password)

        user = User(
            user_name=data.user_name,
            email=data.email,
            hashed_password=hashed_password,
        )

        return await self._repo.create_user(user)
