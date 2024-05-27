from src.core.careers.application.use_cases.list_career import (
    CareerListRequest,
    CareerOutput,
    ListCareer,
)
from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestListCareer:
    def test_list_careers(self):
        career = Career(
            id=1,
            username="username",
            title="title",
            content="content",
        )
        repository = InMemoryCareersRepository(
            careers=[career],
        )
        use_case = ListCareer(repository)

        response = use_case.execute(CareerListRequest)

        assert len(response.data) == 1
        assert response.data[0] == CareerOutput(
            id=1,
            username="username",
            title="title",
            content="content",
            created_datetime=career.created_datetime,
        )
