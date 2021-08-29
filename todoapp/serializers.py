from rest_framework import serializers

from todoapp.models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectSerializer(serializers.ModelSerializer):
    members = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = '__all__'
