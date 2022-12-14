from distutils.command.upload import upload
from email import message
from turtle import title
from django.db import models


class Categories(models.TextChoices):
    LX = 'LX', 'Linux'
    AR = 'AR', 'Arduino'
    RB = 'RB', 'RaspberryPI'
    VI = 'VI', 'VI and VIM'
    PY = 'PY', 'Python'
    DJ = 'DJ', 'Django'


class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    author = models.CharField(max_length=30)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.LX,
    )
    approved = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    def __str__(self) -> str:
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
