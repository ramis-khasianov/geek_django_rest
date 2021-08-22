from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from userapp.models import User


class Command(BaseCommand):
    help = 'Create test author records'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=5)

    def handle(self, *args, **options):
        print(f'Creating Superuser')
        User.objects.create(
            username='django',
            email='django@todoist.com',
            first_name=f'Django',
            last_name=f'Admin',
            password=make_password('geekbrains')
        )

        count = options['count']
        print(f'Creating {count} users')

        for i in range(count):
            user = User.objects.create(
                username=f'username{i}',
                email=f'username{i}@todoist.com',
                first_name=f'Firstname{i}',
                last_name=f'Lastname{i}',
                password=make_password('geekbrains')
            )
            print(f'Created {user}')

        print('Done')
