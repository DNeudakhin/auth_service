from dataclasses import dataclass


@dataclass(slots=True, frozen=True, kw_only=True)
class RegisterUser:
    user_name: str
    email: str
    password: str
