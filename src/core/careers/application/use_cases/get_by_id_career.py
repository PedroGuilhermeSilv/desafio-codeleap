from dataclasses import dataclass
from src.core.careers.domain.careers_repository import CareersRepository
from src.core.careers.application.exceptions import CareerNotFoundError
from datetime import datetime


@dataclass
class CareerGetByIdRequest:
    id: int


@dataclass
class CareerGetByIdResponse:
    id: int
    username: str
    title: str
    content: str
    created_datetime: datetime


class GetByIdCareer:
    def __init__(self, repository: CareersRepository):
        self.repository = repository

    def execute(self, request: CareerGetByIdRequest) -> CareerGetByIdResponse:
        career = self.repository.get_by_id(request.id)
        if not career:
            raise CareerNotFoundError(f"Career with id {request.id} not found")
        return CareerGetByIdResponse(
            id=career.id,
            username=career.username,
            title=career.title,
            content=career.content,
            created_datetime=career.created_datetime,
        )
