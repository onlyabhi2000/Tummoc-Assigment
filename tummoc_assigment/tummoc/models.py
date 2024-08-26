from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
import uuid


class MovieCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title


class Movie(models.Model):
    collection = models.ForeignKey(MovieCollection, on_delete=models.CASCADE, related_name='movies')
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255)
    uuid = models.UUIDField(unique=True)

    def __str__(self):
        return self.title
