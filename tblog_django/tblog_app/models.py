from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=4096, default='')
    body = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.id)


class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=256)


class Post_tag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_name = models.ForeignKey(Tag, on_delete=models.CASCADE)
