from src.core.careers.domain.careers import Career
from src.core.careers.infra.in_memory_careers import InMemoryCareersRepository


class TestSave:
    def test_can_save_a_career(self):
        repository = InMemoryCareersRepository()
        career = Career(id=1, username="username", title="title", content="content")
        repository.save(career)

        assert len(repository.careers) == 1
        assert repository.careers[0] == career
