import pytest
from src.core.careers.domain.careers import Career


class TestCreateCareers:
    def test_username_is_required(self):
        with pytest.raises(ValueError, match="Username is required"):
            Career(id=1, title="Title")

    def test_title_is_required(self):
        with pytest.raises(ValueError, match="Title is required"):
            Career(id=1, username="Username")

    def test_create_careers_with_all_values(self):
        careers = Career(id=1, username="Username", title="Title", content="Content")
        assert careers.id == 1
        assert careers.username == "Username"
        assert careers.title == "Title"
        assert careers.content == "Content"
        assert careers.created_datetime is not None

    def test_username_is_too_long(self):
        with pytest.raises(ValueError, match="Username is too long"):
            Career(id=1, username="Username" * 300, title="Title")
