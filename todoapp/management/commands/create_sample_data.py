from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from todoapp.models import Project, ToDo
from userapp.models import User
import random


class Command(BaseCommand):
    help = 'Create sample projects and todos. you can specify number of projects'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=3)

    def handle(self, *args, **options):
        count = options['count']
        users = list(User.objects.all())

        if users:
            for i in range(count):
                members = random.sample(users, 3)
                project = Project.objects.create(
                    name=f'Project{i}'
                )
                project.members.set(members)
                todos_n = random.randint(1, 4)
                for j in range(todos_n):
                    author = random.choice(members)
                    todo = ToDo.objects.create(
                        project=project,
                        author=author,
                        text=f'ToDo {j} for {project.name} sample text'
                    )
                print(f'Created {project} with {todos_n} todos')
        else:
            print('You must create users via "create_users" command before creating projects')
