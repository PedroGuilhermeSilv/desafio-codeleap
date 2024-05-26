from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestDelete:
    def test_can_delete_a_career(self):
        repository = InMemoryCareersRepository()
        career = Career(id=1, username="username", title="title", content="content")
        repository.save(career)
        repository.delete(1)

        assert len(repository.careers) == 0
