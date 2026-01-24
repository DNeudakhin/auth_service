import uuid

from sqlalchemy import select

from domain import entity
from domain.repository import AbstractUserRepository
from infrastructure.persistence import model
from infrastructure.persistence.manager import DBManager, manager
from infrastructure.persistence.mapper import UserMapper


class SqlAlchemyUserRepository(AbstractUserRepository):
    __slots__ = "_manager"

    def __init__(self) -> None:
        self._manager: DBManager = manager

    async def get_user_by_email(self, email: str) -> entity.User | None:
        async with self._manager.session_maker() as s:
            result = await s.execute(
                select(model.User).where(model.User.email == email)
            )
            user = result.scalar_one_or_none()

        if user:
            return UserMapper.to_domain(user)

        return None

    async def create_user(self, entity: entity.User) -> uuid.UUID:
        async with self._manager.session_maker() as s:
            model = UserMapper.to_orm(entity)
            s.add(model)
            await s.commit()
            await s.refresh(model)

        return model.id
