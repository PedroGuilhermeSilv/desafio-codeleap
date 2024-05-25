from dataclasses import dataclass
from src.core.careers.domain.careers import Career
from src.core.careers.domain.careers_repository import CareersRepository
from src.core.careers.application.exceptions import InvalidCareerData


@dataclass
class CareerCreateRequest:
    username: str
    title: str
    content: str


@dataclass
class CareerCreateResponse:
    id: int


class CreateCareer:
    def __init__(self, repository: CareersRepository):
        self.repository = repository

    def execute(self, request: CareerCreateRequest) -> CareerCreateResponse:
        try:
            career = Career(
                id=self.repository.count() + 1,
                username=request.username,
                title=request.title,
                content=request.content,
            )
            self.repository.save(career)
        except ValueError as err:
            raise InvalidCareerData(str(err)) from err
        return CareerCreateResponse(id=career.id)
