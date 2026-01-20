from typing_extensions import Protocol


class AbstractHasher(Protocol):
    @staticmethod
    def hash(raw_string: str) -> str: ...
    @staticmethod
    def compare(raw_string: str, hashed_string: str) -> bool: ...
