from passlib.context import CryptContext

from core.service import AbstractHasher


class PasslibHasher(AbstractHasher):
    __slots__ = ("_secret_key", "_hasher")

    def __init__(self, secret_key: str) -> None:
        self._secret_key: str = secret_key
        self._hasher: CryptContext = CryptContext(
            schemes=["bcrypt"], default="bcrypt", deprecated="auto"
        )

    def hash(self, plain: str) -> str:
        if not isinstance(plain, str):
            raise ValueError(
                "The value must be a string,"
                f"but the type passed is {type(plain)}"
            )
        return self._hasher.hash(f"{plain}{self._secret_key}")

    def compare(self, plain: str, hashed: str) -> bool:
        if not isinstance(plain, str):
            raise ValueError(
                "The value must be a string,"
                f"but the type passed is {type(plain)}"
            )
        return self._hasher.verify(f"{plain}{self._secret_key}", hashed)
