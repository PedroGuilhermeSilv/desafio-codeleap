from dataclasses import dataclass
from src.core.careers.application.exceptions import (
    InvalidCareerData,
    CareerNotFoundError,
)


@dataclass
class CareerUpdatedRequest:
    title: str
    content: str


class UpdatedCareer:
    def __init__(self, repository: CareerUpdatedRequest):
        self.repository = repository

    def execute(self, request: CareerUpdatedRequest, id: int) -> None:
        caree = self.repository.get_by_id(id)
        if not caree:
            raise CareerNotFoundError(f"Career with id {id} not found")
        try:
            caree.update(
                title=request.title,
                content=request.content,
            )
            self.repository.save(caree)
        except ValueError as err:
            raise InvalidCareerData(str(err)) from err
