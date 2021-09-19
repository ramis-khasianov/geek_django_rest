from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email', unique=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['id']
