from rest_framework import mixins, viewsets

from userapp.models import User
from userapp.serializers import UserSerializer


class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()  # Честно, не додумался бы не посмотрев 5ый урок :)
