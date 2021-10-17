from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


class Category(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
