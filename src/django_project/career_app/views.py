from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from src.core.careers.application.exceptions import CareerNotFoundError
from src.core.careers.application.use_cases.create_career import (
    CareerCreateRequest,
    CreateCareer,
)
from src.core.careers.application.use_cases.delete_career import (
    CareerDeleteRequest,
    DeleteCareer,
)
from src.core.careers.application.use_cases.get_by_id_career import (
    CareerGetByIdRequest,
    GetByIdCareer,
)
from src.core.careers.application.use_cases.list_career import (
    CareerListRequest,
    ListCareer,
)
from src.core.careers.application.use_cases.updated_career import (
    CareerUpdatedRequest,
    UpdatedCareer,
)
from src.django_project.career_app.models import Career as CareerModel
from src.django_project.career_app.repository import DjangoORMCareersRepository
from src.django_project.career_app.serializers import (
    CreateCareerRequestSerializer,
    CreateCareerResponseSerializer,
    DeleteCareerRequestSerializer,
    ListCareerResponseSerializer,
    RetrieveCareerRequestSerializer,
    RetrieveCareerResponseSerializer,
    UpdateCareerRequestSerializer,
)


class CareerViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        use_case = ListCareer(repository=DjangoORMCareersRepository(CareerModel))

        response = use_case.execute(request=CareerListRequest())
        serializer = ListCareerResponseSerializer(instance=response)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request: Request, pk=None) -> Response:
        serializer = RetrieveCareerRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)
        career_id = pk

        try:
            use_case = GetByIdCareer(
                repository=DjangoORMCareersRepository(CareerModel),
            )
            result = use_case.execute(CareerGetByIdRequest(id=career_id))
        except CareerNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = RetrieveCareerResponseSerializer(instance=result)
        response = serializer.data
        return Response(status=status.HTTP_200_OK, data=response)

    def create(self, request: Request) -> Response:
        serializer = CreateCareerRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            use_case = CreateCareer(
                repository=DjangoORMCareersRepository(CareerModel),
            )
            result = use_case.execute(
                CareerCreateRequest(**serializer.validated_data),
            )
            response = CreateCareerResponseSerializer(instance=result)

        except CareerNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_201_CREATED, data=response.data)

    def partial_update(self, request: Request, pk=None) -> Response:
        serializer = UpdateCareerRequestSerializer(
            data={
                **request.data,
                "id": pk,
            },
        )
        serializer.is_valid(raise_exception=True)

        try:
            use_case = UpdatedCareer(
                repository=DjangoORMCareersRepository(CareerModel),
            )
            use_case.execute(
                CareerUpdatedRequest(
                    title=serializer.validated_data["title"],
                    content=serializer.validated_data["content"],
                ),
                id=serializer.validated_data["id"],
            )
        except CareerNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Career not found")

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data="Careers updated successfully",
        )

    def destroy(self, request: Request, pk=None) -> Response:
        serializer = DeleteCareerRequestSerializer(data={"id": pk})
        serializer.is_valid(raise_exception=True)

        try:
            use_case = DeleteCareer(
                repository=DjangoORMCareersRepository(CareerModel),
            )
            use_case.execute(CareerDeleteRequest(id=serializer.validated_data["id"]))
        except CareerNotFoundError:
            return Response(status=status.HTTP_404_NOT_FOUND, data="Career not found")

        return Response(
            status=status.HTTP_204_NO_CONTENT,
            data="{}",
        )
