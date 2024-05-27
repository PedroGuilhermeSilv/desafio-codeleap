import pytest

from src.core.careers.domain.careers import Career
from src.django_project.career_app.models import Career as CareerModel
from src.django_project.career_app.repository import DjangoORMCareersRepository


@pytest.mark.django_db
class TestSave:
    def test_save_career_in_db(self):
        career = Career(
            username="username",
            title="title",
            content="content",
        )
        repository = DjangoORMCareersRepository(CareerModel)

        repository.save(career)

        career_db = CareerModel.objects.first()
        assert career_db.username == "username"
        assert career_db.title == "title"
        assert career_db.content == "content"


@pytest.mark.django_db
class TestGetById:
    def test_get_career_by_id(self):
        career = Career(
            username="username",
            title="title",
            content="content",
        )
        repository = DjangoORMCareersRepository(CareerModel)
        career_db = CareerModel.objects.create(
            username=career.username,
            title=career.title,
            content=career.content,
        )

        career_db = repository.get_by_id(career_db.id)

        assert career_db.username == "username"
        assert career_db.title == "title"
        assert career_db.content == "content"

    def test_get_carer_by_id_not_found(self):
        repository = DjangoORMCareersRepository(CareerModel)

        career_db = repository.get_by_id(1)

        assert career_db is None


@pytest.mark.django_db
class TestDelete:
    def test_delete_career_by_id(self):
        career = Career(
            username="username",
            title="title",
            content="content",
        )
        repository = DjangoORMCareersRepository(CareerModel)
        career_orm = CareerModel.objects.create(
            username=career.username,
            title=career.title,
            content=career.content,
        )

        assert CareerModel.objects.count() == 1

        repository.delete(career_orm.id)

        assert CareerModel.objects.count() == 0

    def test_delete_career_by_id_not_found(self):
        repository = DjangoORMCareersRepository(CareerModel)

        repository.delete(1)

        assert CareerModel.objects.count() == 0


@pytest.mark.django_db
class TestList:
    def test_list_careers(self):
        career_1 = Career(
            username="username 1",
            title="title 1",
            content="content 1",
        )
        career_2 = Career(
            username="username 2",
            title="title 2",
            content="content 2",
        )
        repository = DjangoORMCareersRepository(CareerModel)
        career_orm_1 = CareerModel.objects.create(
            username=career_1.username,
            title=career_1.title,
            content=career_1.content,
        )
        career_orm_2 = CareerModel.objects.create(
            username=career_2.username,
            title=career_2.title,
            content=career_2.content,
        )

        careers = repository.list()

        length = CareerModel.objects.count()
        assert len(careers) == length
        assert careers[0].id == career_orm_1.id
        assert careers[0].username == career_orm_1.username
        assert careers[0].title == career_orm_1.title
        assert careers[0].content == career_orm_1.content
        assert careers[1].id == career_orm_2.id
        assert careers[1].username == career_orm_2.username
        assert careers[1].title == career_orm_2.title
        assert careers[1].content == career_orm_2.content

    def test_list_careers_empty(self):
        repository = DjangoORMCareersRepository(CareerModel)

        careers = repository.list()

        assert len(careers) == 0


@pytest.mark.django_db
class TestUpdate:
    def test_update_career(self):
        career = Career(
            username="username",
            title="title",
            content="content",
        )
        repository = DjangoORMCareersRepository(CareerModel)

        career_db = CareerModel.objects.create(
            username=career.username,
            title=career.title,
            content=career.content,
        )

        career.title = "title updated"
        career.content = "content updated"
        repository.update(career, career_db.id)

        career_db = CareerModel.objects.get(id=career_db.id)
        assert career_db.title == "title updated"
        assert career_db.content == "content updated"
