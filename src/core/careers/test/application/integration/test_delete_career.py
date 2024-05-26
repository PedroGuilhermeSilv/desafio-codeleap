import pytest
from src.core.careers.application.exceptions import CareerNotFoundError
from src.core.careers.application.use_cases.delete_career import (
    CareerDeleteRequest,
    DeleteCareer,
)
from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestDeleteCareer:
    def test_can_delete_a_career_not_exist(self):
        repository = InMemoryCareersRepository()
        use_case = DeleteCareer(repository)
        request = CareerDeleteRequest(id=1)

        pytest.raises(CareerNotFoundError, use_case.execute, request)

    def test_can_delete_a_career(self):
        repository = InMemoryCareersRepository(
            careers=[
                Career(id=1, username="username", title="title", content="content"),
            ],
        )
        use_case = DeleteCareer(repository)
        request = CareerDeleteRequest(id=1)

        response = use_case.execute(request)
        response is None
        assert len(repository.careers) == 0
