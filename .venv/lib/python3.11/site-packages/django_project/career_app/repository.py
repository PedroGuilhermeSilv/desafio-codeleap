from src.core.careers.domain.careers import Career
from src.core.careers.domain.careers_repository import CareersRepository
from src.django_project.career_app.models import Career as CareerModel


class DjangoORMCareersRepository(CareersRepository):
    def __init__(self, career_model: CareerModel):
        self.career_model = career_model

    def save(self, career: Career) -> None:
        self.career_model.objects.create(
            username=career.username,
            title=career.title,
            content=career.content,
            created_datetime=career.created_datetime,
        )

    def get_by_id(self, id: int) -> Career | None:
        if career := self.career_model.objects.filter(id=id).first():
            return Career(
                id=career.id,
                username=career.username,
                title=career.title,
                content=career.content,
            )
        return None

    def delete(self, id: int) -> None:
        self.career_model.objects.filter(id=id).delete()

    def list(self) -> list[Career] | None:
        return [
            Career(
                id=career.id,
                username=career.username,
                title=career.title,
                content=career.content,
            )
            for career in self.career_model.objects.all()
        ]

    def update(self, career: Career, id: int) -> None:
        CareerModel.objects.filter(id=id).update(
            title=career.title or career.title,
            content=career.content or career.content,
        )

    def count(self) -> int:
        return self.career_model.objects.count()
