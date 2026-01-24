from dataclasses import dataclass


@dataclass(slots=True, frozen=True, kw_only=True)
class RegisterUserComand:
    user_name: str
    email: str
    password: str
