from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient
from userapp.views import UsersViewSet


class TestUserViewSet(TestCase):

    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            'django', 'django@todoist.com', 'geekbrains'
        )
        self.user_data = {
            'username': 'francis.bacon',
            'firstName': 'Francis',
            'lastName': 'Bacon',
            'email': 'francis.bacon@todoist.com'
        }

    def test_get_list_as_guest(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UsersViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_as_superuser(self):
        factory = APIRequestFactory()
        request = factory.get('api/users/')
        view = UsersViewSet.as_view({'get': 'list'})
        force_authenticate(request, self.superuser)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_as_guest(self):
        user = get_user_model().objects.create_user(
            'test', 'test@todoist.com', 'geekbrains'
        )
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_as_superuser(self):
        user = get_user_model().objects.create_user(
            'test', 'test@todoist.com', 'geekbrains'
        )
        client = APIClient()
        client.login(username='django', password='geekbrains')
        response = client.put(f'/api/users/{user.id}/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)




