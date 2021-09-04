from django_filters import rest_framework as filters
from todoapp.models import ToDo


class ToDoFilter(filters.FilterSet):
    created = filters.DateFromToRangeFilter()
    project = filters.CharFilter(field_name='project__name', lookup_expr='contains')

    class Meta:
        model = ToDo
        fields = ['created', 'project']
