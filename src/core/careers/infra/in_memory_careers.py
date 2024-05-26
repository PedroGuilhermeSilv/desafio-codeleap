from src.core.careers.domain.careers import Career
from src.core.careers.domain.careers_repository import CareersRepository


class InMemoryCareersRepository(CareersRepository):
    def __init__(self, careers=None):
        self.careers = careers or []

    def save(self, career):
        self.careers.append(career)

    def get_by_id(self, id: int) -> Career | None:
        return next((career for career in self.careers if career.id == id), None)

    def delete(self, id: int) -> None:
        self.careers.remove(self.get_by_id(id))

    def update(self, career: Career, id: int) -> None:
        for careers in self.careers:
            if careers.id == id:
                careers.title = career.title
                careers.content = career.content

    def count(self) -> int:
        return len(self.careers)

    def list(self) -> list[Career]:
        return list(self.careers)
