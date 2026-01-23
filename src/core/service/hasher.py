import abc


class AbstractHasher(abc.ABC):
    @abc.abstractmethod
    def hash(self, plain: str) -> str: ...

    @abc.abstractmethod
    def compare(self, plain: str, hashed: str) -> bool: ...


class FakeHasher(AbstractHasher):
    def __init__(self, password: str, is_compare: bool = True):
        self._hashed_password: str = password
        self._is_compare: bool = is_compare

    def hash(self, plain: str) -> str:
        return self._hashed_password

    def compare(self, plain: str, hashed: str) -> bool:
        return self._is_compare
