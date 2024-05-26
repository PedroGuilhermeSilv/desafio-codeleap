import json
from datetime import UTC, datetime

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from src.core.careers.domain.careers import Career
from src.django_project.career_app.models import Career as CareerModel
from src.django_project.career_app.repository import DjangoORMCareersRepository


@pytest.fixture
def career_1() -> Career:
    return Career(
        username="username",
        title="title",
        content="content",
    )


@pytest.fixture
def career_2() -> Career:
    return Career(
        username="username2",
        title="title2",
        content="content2",
    )


@pytest.fixture
def career_repository() -> DjangoORMCareersRepository:
    return DjangoORMCareersRepository(CareerModel)


@pytest.mark.django_db
class TestListAPI:
    def test_list_category(
        self,
        career_1: Career,
        career_2: Career,
        career_repository: DjangoORMCareersRepository,
    ):
        repository = career_repository
        repository.save(career_1)
        repository.save(career_2)

        response = APIClient().get("/careers/")
        assert response.data == {
            "data": [
                {
                    "id": 1,
                    "username": "username",
                    "title": "title",
                    "content": "content",
                    "created_datetime": response.data["data"][0]["created_datetime"],
                },
                {
                    "id": 2,
                    "username": "username2",
                    "title": "title2",
                    "content": "content2",
                    "created_datetime": response.data["data"][1]["created_datetime"],
                },
            ],
        }
        assert response.status_code == status.HTTP_200_OK

        length = CareerModel.objects.count()
        assert len(response.data["data"]) == length


@pytest.mark.django_db
class TestCreateAPI:
    def test_when_payload_is_invalid_then_return_400(self):
        response = APIClient().post(
            "/careers/",
            data={
                "username": "",
                "title": "title",
                "content": "asdf",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {"username": ["This field may not be blank."]}

    def test_return_201_when_payload_is_valid(self):
        response = APIClient().post(
            "/careers/",
            data={
                "username": "username",
                "title": "title",
                "content": "content",
            },
        )

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {
            "id": response.data["id"],
        }


@pytest.mark.django_db
class TestRetrieveAPI:
    def test_return_careers_when_exists(self):
        career = CareerModel.objects.create(
            id=1,
            username="username",
            title="title",
            content="content",
            created_datetime=datetime.now(tz=(UTC)),
        )

        response = APIClient().get(f"/careers/{career.id}/")

        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "data": {
                "id": career.id,
                "username": career.username,
                "title": career.title,
                "content": career.content,
                "created_datetime": career.created_datetime.strftime(
                    "%Y-%m-%dT%H:%M",
                ),
            },
        }

    def test_return_404_when_career_not_exists(self):
        response = APIClient().get("/careers/1/")

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestDeleteAPI:
    def test_return_204_delete_sucess(self):
        career = CareerModel.objects.create(
            id=1,
            username="username",
            title="title",
            content="content",
            created_datetime=datetime.now(tz=(UTC)),
        )

        response = APIClient().delete(f"/careers/{career.id}/")

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data == "{}"

    def test_return_404_when_career_not_exists(self):
        response = APIClient().delete("/careers/1/")

        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestUpdateAPI:
    def test_return_204_updated_sucess(self):
        career = CareerModel.objects.create(
            id=1,
            username="username",
            title="title",
            content="content",
            created_datetime=datetime.now(tz=(UTC)),
        )

        body = json.dumps(
            {
                "title": "title updated",
                "content": "content updated",
            },
        )
        response = APIClient().patch(
            f"/careers/{career.id}/",
            content_type="application/json",
            data=body,
        )

        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.data == "Careers updated successfully"

        career_updated = CareerModel.objects.get(id=career.id)
        assert career_updated.title == "title updated"
        assert career_updated.content == "content updated"

    def test_return_404_when_career_not_exists(self):
        body = json.dumps(
            {
                "title": "title updated",
                "content": "content updated",
            },
        )
        response = APIClient().patch(
            f"/careers/{1}/",
            content_type="application/json",
            data=body,
        )

        assert response.data == "Career not found"
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_return_400_when_payload_is_invalid(self):
        body = json.dumps(
            {
                "title": "",
                "content": "content updated",
            },
        )
        response = APIClient().patch(
            f"/careers/{1}/",
            content_type="application/json",
            data=body,
        )

        assert response.data == {"title": ["This field may not be blank."]}
        assert response.status_code == status.HTTP_400_BAD_REQUEST
