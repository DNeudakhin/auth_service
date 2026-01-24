from domain import entity
from infrastructure.persistence import model


class UserMapper:
    @staticmethod
    def to_domain(user: model.User) -> entity.User:
        return entity.User.from_persistence_storage(
            id=user.id,
            user_name=user.user_name,
            email=user.email,
            hashed_password=user.password,
        )

    @staticmethod
    def to_orm(user: entity.User) -> model.User:
        return model.User(
            id=user.id,
            user_name=user.user_name,
            email=user.email,
            password=user.password,
        )
