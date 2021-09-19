from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ToDoSerializer, ProjectSerializerBase


class ProjectPagination(PageNumberPagination):
    page_size = 10


class ToDoPagination(PageNumberPagination):
    page_size = 20


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializerBase
    queryset = Project.objects.all()
    pagination_class = ProjectPagination

    def get_queryset(self):
        queryset = Project.objects.all()
        name = self.request.query_params.get('name', None)
        if name:
            queryset = queryset.filter(name__contains=name)
        return queryset


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ToDoFilter

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        todo.is_active = False
        todo.save()
        """
        Я честно покликал в постмане, чтобы понять какая ошибка тут может вывалиться
        Но он мне просто сразу выдает NotFound с методом DELETE на несусществующую запись
        А писать голый except мне чет некомфортно. 
        """
        return Response(status=status.HTTP_204_NO_CONTENT)
