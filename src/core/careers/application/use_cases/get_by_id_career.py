from dataclasses import dataclass
from datetime import datetime

from src.core.careers.application.exceptions import CareerNotFoundError
from src.core.careers.domain.careers_repository import CareersRepository


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
            error = f"Career with id {request.id} not found"
            raise CareerNotFoundError(error)
        return CareerGetByIdResponse(
            id=career.id,
            username=career.username,
            title=career.title,
            content=career.content,
            created_datetime=career.created_datetime,
        )
