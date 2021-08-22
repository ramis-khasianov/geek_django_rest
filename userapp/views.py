from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from userapp.models import User
from userapp.serializers import UserModelSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
