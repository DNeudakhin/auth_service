import uuid

from sqlalchemy import select

from domain import entity
from infrastructure.persistence import model
from infrastructure.persistence.manager import DBManager
from infrastructure.persistence.mapper import UserMapper


class SqlAlchemyUserRepository:
    __slots__ = "_manager"

    def __init__(self, manager: DBManager) -> None:
        self._manager: DBManager = manager

    async def get_user_by_id(self, id: uuid.UUID) -> entity.User | None:
        async with self._manager.session_maker() as s:
            result = await s.execute(
                select(model.User).where(model.User.id == id)
            )
            user = result.scalar_one_or_none()

        if user:
            return UserMapper.to_domain(user)

        return None

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
