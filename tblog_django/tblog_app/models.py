from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=4096, default='')
    body = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return str(self.id)
