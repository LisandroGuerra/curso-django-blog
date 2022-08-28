from turtle import title
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self) -> str:
        return self.title
