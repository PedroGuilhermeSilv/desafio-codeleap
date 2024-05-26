import pytest
from src.core.careers.domain.careers import Career


class TestEquality:
    def test_id_equals(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        other_careers = Career(
            id=1,
            username="Username",
            title="Title",
            content="Content",
        )
        assert careers == other_careers

    def test_id_not_equals(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        other_careers = Career(
            id=2,
            username="Username",
            title="Title",
            content="Content",
        )
        assert careers != other_careers

    def test_equality_different_classes(self):
        class Dummy:
            pass

        careers = Career(id=1, username="Username", title="Title", content="Content")
        dummy = Dummy()
        dummy.id = 1
        with pytest.raises(ValueError, match="Comparison between different classes"):
            careers == dummy
