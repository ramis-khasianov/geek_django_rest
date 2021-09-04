from django.db import models

from userapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=255)
    repository = models.URLField()
    members = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project = models.ForeignKey(Project, related_name='todos', on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Todo {self.pk} for {self.project.name} by {self.author}'
