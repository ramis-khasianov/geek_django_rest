from rest_framework import serializers

from todoapp.models import Project, ToDo
from userapp.serializers import UserSerializer


class ToDoSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectToDoSerializer(serializers.ModelSerializer):
    """
    Lighter version serializer for using inside Project serializer
    """

    class Meta:
        model = ToDo
        fields = ['text', 'author', 'created', 'is_active']


class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True)
    todos = ProjectToDoSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'url', 'name', 'repository', 'todos', 'members']
