from rest_framework.viewsets import ModelViewSet

from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectSerializer, ToDoSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
