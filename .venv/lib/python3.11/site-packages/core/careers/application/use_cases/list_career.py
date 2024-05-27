from dataclasses import dataclass
from datetime import datetime

from src.core.careers.domain.careers_repository import CareersRepository


@dataclass
class CareerOutput:
    id: int
    username: str
    title: str
    content: str
    created_datetime: datetime


@dataclass
class CareerListResponse:
    data: list[CareerOutput]


@dataclass
class CareerListRequest:
    pass


class ListCareer:
    def __init__(self, repository: CareersRepository):
        self.repository = repository

    def execute(self, request: CareerListRequest) -> CareerListResponse:
        careers = self.repository.list()
        return CareerListResponse(
            data=[
                CareerOutput(
                    id=career.id,
                    username=career.username,
                    title=career.title,
                    content=career.content,
                    created_datetime=career.created_datetime,
                )
                for career in careers
            ],
        )
