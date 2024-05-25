from src.core.careers.application.use_cases.updated_career import (
    CareerUpdatedRequest,
    UpdatedCareer,
)
from src.core.careers.application.exceptions import (
    InvalidCareerData,
    CareerNotFoundError,
)
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository
from src.core.careers.domain.careers import Career
import pytest


class TestUpdatedCareer:
    def test_can_update_a_career(self):
        repository = InMemoryCareersRepository(
            careers=[
                Career(id=1, username="username", title="title", content="content")
            ]
        )
        use_case = UpdatedCareer(repository)
        request = CareerUpdatedRequest(title="title updated", content="content updated")

        use_case.execute(request, id=1)

        career = repository.get_by_id(1)
        assert career.title == "title updated"
        assert career.content == "content updated"

    def test_cannot_update_a_career_not_exist(self):
        repository = InMemoryCareersRepository()
        use_case = UpdatedCareer(repository)
        request = CareerUpdatedRequest(title="title updated", content="content updated")

        pytest.raises(CareerNotFoundError, use_case.execute, request, 1)

    def test_cannot_update_a_career_with_invalid_data(self):
        repository = InMemoryCareersRepository(
            careers=[
                Career(id=1, username="username", title="title", content="content")
            ]
        )
        use_case = UpdatedCareer(repository)

        pytest.raises(
            InvalidCareerData,
            use_case.execute,
            CareerUpdatedRequest(title="", content="content updated"),
            1,
        )

    def test_cannot_update_a_career_with_invalid_data_2(self):
        repository = InMemoryCareersRepository(
            careers=[
                Career(id=1, username="username", title="title", content="content")
            ]
        )
        use_case = UpdatedCareer(repository)

        pytest.raises(
            InvalidCareerData,
            use_case.execute,
            CareerUpdatedRequest(title="title updated", content=""),
            1,
        )
