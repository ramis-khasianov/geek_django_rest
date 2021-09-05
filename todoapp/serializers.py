from rest_framework import serializers

from todoapp.models import Project, ToDo
from userapp.serializers import UserSerializer


class ToDoSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = ToDo
        fields = ['id', 'text', 'author', 'created', 'is_active']


class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    todos = ToDoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'url', 'name', 'repository', 'todos', 'members']
