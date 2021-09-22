from rest_framework import mixins, viewsets

from userapp.models import User
from userapp.serializers import UserSerializer, UserSerializerV2


class UsersViewSet(mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   viewsets.GenericViewSet):

    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '1.0':
            return UserSerializer
        return UserSerializerV2

