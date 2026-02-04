import uuid


class User:
    __slots__ = ("id", "user_name", "email", "password")

    def __init__(
        self,
        user_name: str,
        email: str,
        hashed_password: str | None = None,
        id: uuid.UUID | None = None,
    ) -> None:
        self.id: uuid.UUID = id if id else uuid.uuid4()
        self.user_name: str = user_name
        self.email: str = email
        self.password: str | None = hashed_password
