from typing_extensions import Protocol


class Hasher(Protocol):
    def hash(self, plain: str) -> str: ...

    def compare(self, plain: str, hashed: str) -> bool: ...
