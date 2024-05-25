from dataclasses import dataclass

from src.core.careers.application.exceptions import (
    CareerNotFoundError,
    InvalidCareerDataErrorError,
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
            error = f"Career with id {id} not found"
            raise CareerNotFoundError(error)
        try:
            caree.update(
                title=request.title,
                content=request.content,
            )
            self.repository.save(caree)
        except ValueError as err:
            raise InvalidCareerDataErrorError(str(err)) from err
