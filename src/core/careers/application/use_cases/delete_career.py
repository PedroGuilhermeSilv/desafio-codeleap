from dataclasses import dataclass
from src.core.careers.domain.careers_repository import CareersRepository
from src.core.careers.application.exceptions import CareerNotFoundError


@dataclass
class CareerDeleteRequest:
    id: int


class DeleteCareer:
    def __init__(self, repository: CareersRepository):
        self.repository = repository

    def execute(self, request: CareerDeleteRequest) -> None:
        try:
            self.repository.get_by_id(request.id)
            if not self.repository.get_by_id(request.id):
                raise CareerNotFoundError(f"Career with id {request.id} not found")
            self.repository.delete(request.id)
        except ValueError as err:
            raise CareerNotFoundError(str(err)) from err
