import pytest
from src.core.careers.domain.careers import Career


class TestCreateCarrers:
    def test_username_is_required(self):
        with pytest.raises(ValueError, match="Username is required"):
            Career(id=1, title="Title")

    def test_title_is_required(self):
        with pytest.raises(ValueError, match="Title is required"):
            Career(id=1, username="Username")

    def test_create_carrers_with_all_values(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        assert carrers.id == 1
        assert carrers.username == "Username"
        assert carrers.title == "Title"
        assert carrers.content == "Content"
        assert carrers.created_datetime is not None

    def test_username_is_too_long(self):
        with pytest.raises(ValueError, match="Username is too long"):
            Career(id=1, username="Username" * 10, title="Title")


class TestChangeCarrers:
    def test_change_title_valid(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        carrers.update(title="New Title", content="Content")
        assert carrers.title == "New Title"

    def test_change_content_valid(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        carrers.update(title="Title", content="New Content")
        assert carrers.content == "New Content"

    def test_change_content_empty(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        with pytest.raises(ValueError, match="Content is required"):
            carrers.update(title="Title", content="")

    def test_change_title_empty(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        with pytest.raises(ValueError, match="Title is required"):
            carrers.update(title="", content="Content")


class TestEquality:
    def test_id_equals(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        other_carrers = Career(
            id=1,
            username="Username",
            title="Title",
            content="Content",
        )
        assert carrers == other_carrers

    def test_id_not_equals(self):
        carrers = Career(id=1, username="Username", title="Title", content="Content")
        other_carrers = Career(
            id=2,
            username="Username",
            title="Title",
            content="Content",
        )
        assert carrers != other_carrers

    def test_equality_different_classes(self):
        class Dummy:
            pass

        carrers = Career(id=1, username="Username", title="Title", content="Content")
        dummy = Dummy()
        dummy.id = 1
        with pytest.raises(ValueError, match="Comparison between different classes"):
            carrers == dummy
