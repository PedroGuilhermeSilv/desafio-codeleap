from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestList:
    def test_can_list_careers(self):
        career = Career(id=1, username="username", title="title", content="content")
        repository = InMemoryCareersRepository(
            careers=[career],
        )
        repository.list()

        assert len(repository.careers) == 1
        assert repository.careers[0] == career
