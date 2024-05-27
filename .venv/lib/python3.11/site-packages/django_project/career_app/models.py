from django.db import models

from src.core.careers.domain.careers import MAX_LENGTH


class Career(models.Model):
    username = models.CharField(max_length=MAX_LENGTH)
    title = models.CharField(max_length=MAX_LENGTH)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "careers"
