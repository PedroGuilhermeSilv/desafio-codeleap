import pytest
from src.core.careers.domain.careers import Career


class TestChangeCareers:
    def test_change_title_valid(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        careers.update(title="New Title", content="Content")
        assert careers.title == "New Title"

    def test_change_content_valid(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        careers.update(title="Title", content="New Content")
        assert careers.content == "New Content"

    def test_change_content_empty(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        with pytest.raises(ValueError, match="Content is required"):
            careers.update(title="Title", content="")

    def test_change_title_empty(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        with pytest.raises(ValueError, match="Title is required"):
            careers.update(title="", content="Content")
