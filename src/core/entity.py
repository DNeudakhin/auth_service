import uuid

from typing_extensions import Any


class Entity:
    __slots__ = ("_id",)

    def __init__(self, id: uuid.UUID | None = None):
        self._id: uuid.UUID = id if id else uuid.uuid4()

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Entity):
            return NotImplemented
        return other.id == self.id

    def __hash__(self) -> int:
        return hash(self._id)

    @property
    def id(self) -> uuid.UUID:
        return self._id
