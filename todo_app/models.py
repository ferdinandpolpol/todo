

from django.db import models
from django import forms
from django.conf import settings


class Todo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)