import uuid

from application.dtos.commands.auth import RegisterUserComand
from core.service import AbstractHasher
from domain.entity import User
from domain.repository import AbstractUserRepository


class UserRegisterService:
    __slots__ = ("_repo", "_hasher")

    def __init__(
        self, repo: AbstractUserRepository, hasher: AbstractHasher
    ) -> None:
        self._repo: AbstractUserRepository = repo
        self._hasher: AbstractHasher = hasher

    def execute(self, command: RegisterUserComand) -> uuid.UUID:
        user = User.create(
            user_name=command.user_name,
            email=command.email,
            password=command.password,
            hasher=self._hasher,
        )

        return self._repo.create_user(user)
