import pytest
from src.core.careers.application.exceptions import CareerNotFoundError
from src.core.careers.application.use_cases.get_by_id_career import (
    CareerGetByIdRequest,
    GetByIdCareer,
)
from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestGetByIdCareer:
    def test_can_get_by_id_a_career_not_exist(self):
        repository = InMemoryCareersRepository()
        use_case = GetByIdCareer(repository)
        request = CareerGetByIdRequest(id=1)

        pytest.raises(CareerNotFoundError, use_case.execute, request)

    def test_can_get_by_id_a_career(self):
        repository = InMemoryCareersRepository(
            careers=[
                Career(id=1, username="username", title="title", content="content"),
            ],
        )
        use_case = GetByIdCareer(repository)
        request = CareerGetByIdRequest(id=1)

        response = use_case.execute(request)
        assert response.id == 1
        assert response.username == "username"
        assert response.title == "title"
        assert response.content == "content"
        assert response.created_datetime is not None
