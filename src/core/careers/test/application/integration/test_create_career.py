import pytest
from src.core.careers.application.exceptions import InvalidCareerDataErrorError
from src.core.careers.application.use_cases.create_career import (
    CareerCreateRequest,
    CareerCreateResponse,
    CreateCareer,
)
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestCreateCareer:
    def test_can_create_a_career(self):
        repository = InMemoryCareersRepository()
        use_case = CreateCareer(repository)
        request = CareerCreateRequest(
            username="username",
            title="title",
            content="content",
        )

        response = use_case.execute(request)

        isinstance(response, CareerCreateResponse)

        assert len(repository.careers) == 1
        assert response.id == 1

    def test_cannot_create_a_career_with_invalid_data(self):
        repository = InMemoryCareersRepository()
        use_case = CreateCareer(repository)

        pytest.raises(
            InvalidCareerDataErrorError,
            use_case.execute,
            CareerCreateRequest(username="", title="title", content="content"),
        )

    def test_cannot_create_a_career_with_invalid_data_2(self):
        repository = InMemoryCareersRepository()
        use_case = CreateCareer(repository)

        pytest.raises(
            InvalidCareerDataErrorError,
            use_case.execute,
            CareerCreateRequest(username="username", title="", content="content"),
        )

    def test_cannot_create_a_career_with_invalid_data_3(self):
        repository = InMemoryCareersRepository()
        use_case = CreateCareer(repository)

        pytest.raises(
            InvalidCareerDataErrorError,
            use_case.execute,
            CareerCreateRequest(username="username", title="title", content=""),
        )
