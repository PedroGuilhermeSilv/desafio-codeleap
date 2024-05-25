from abc import ABC, abstractmethod

from src.core.careers.domain.careers import Career


class CareersRepository(ABC):
    @abstractmethod
    def save(self, careers: Career):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Career | None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, careers) -> None:
        raise NotImplementedError

    @abstractmethod
    def count(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[Career]:
        raise NotImplementedError
