from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todoapp.views import ProjectViewSet, ToDoViewSet
from userapp.views import UsersViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Library",
      default_version='0.1',
      description="Documentation to todoist project",
      contact=openapi.Contact(email="admin@admin.local"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny, )
)

router = DefaultRouter()
router.register('users', UsersViewSet)
router.register('projects', ProjectViewSet)
router.register('todos', ToDoViewSet)

urlpatterns = [
    re_path(r'^api/(?P<version>\d\.\d)/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/token-auth/', obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('schema/', schema_view),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

