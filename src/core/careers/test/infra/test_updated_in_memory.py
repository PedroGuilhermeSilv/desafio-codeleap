from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestUpdate:
    def test_can_update_a_career(self):
        repository = InMemoryCareersRepository()
        career = Career(id=1, username="username", title="title", content="content")
        repository.save(career)
        career = Career(
            id=1, username="username", title="new title", content="new content"
        )
        repository.update(career)

        assert len(repository.careers) == 1
        assert repository.careers[0] == career
