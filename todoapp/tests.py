import coreapi
from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APITestCase
from todoapp.models import Project, ToDo


class TestToDoViewSet(APITestCase):

    def setUp(self):
        self.superuser = get_user_model().objects.create_superuser(
            'django', 'django@todoist.com', 'geekbrains'
        )
        self.todo_data = {
            'text': 'Test case todo',
            'author': self.superuser
        }
        self.project_data = {
            'name': 'Test project',
            'repository': 'http://Repository.git'
        }

    def test_get_list_as_guest(self):
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_as_superuser(self):
        self.client.login(username='django', password='geekbrains')
        response = self.client.get('/api/todos/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_as_superuser(self):
        self.client.login(username='django', password='geekbrains')
        project = Project.objects.create(**self.project_data)
        todo = ToDo.objects.create(**self.todo_data, project=project)
        response = self.client.put(
            f'/api/todos/{todo.id}/',
            {
                'text': 'Altered test case todo',
                'author': self.superuser.id,
                'project': project.id
            })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        todo = ToDo.objects.get(id=todo.id)
        self.assertEqual(todo.text, 'Altered test case todo')

    def test_create_project(self):
        self.client.login(username='django', password='geekbrains')
        project = mixer.blend(Project)
        response = self.client.post(
            f'/api/projects/',
            {
                'name': project.name,
                'repository': project.repository
            })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_live_get_list(self):
        client = coreapi.Client()
        schema = client.get('http://localhost:8000/schema/')
        action = ['token-auth', 'create']
        params = {'username': 'django', 'password': 'geekbrains'}
        result = client.action(schema, action, params, validate=True)
        auth = coreapi.auth.TokenAuthentication(
            scheme='Token',
            token=result['token']
        )
        client = coreapi.Client(auth=auth)

        schema = client.get('http://localhost:8000/schema/')

        action = ['projects', 'list']
        data = client.action(schema, action)
        self.assertGreater(data['count'], 0)


