from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_yaml.renderers import YAMLRenderer

from todoapp.views import ProjectViewSet, ToDoViewSet
from userapp.views import UsersViewSet

schema_view = get_schema_view(
    title="ToDoist API",
    permission_classes=[IsAuthenticatedOrReadOnly]
)

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('schema/', schema_view)
]

