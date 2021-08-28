from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from userapp.models import User


class Command(BaseCommand):
    help = 'Create test users records'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=5)

    def handle(self, *args, **options):

        try:
            print(f'Creating Superuser')
            User.objects.create_superuser(
                username='django',
                email='django@todoist.com',
                password='geekbrains',
                first_name='Django',
                last_name='Admin'
            )

            count = options['count']
            print(f'Creating {count} users')

            for i in range(count):
                user = User.objects.create_user(
                    username=f'username{i}',
                    email=f'username{i}@todoist.com',
                    password='geekbrains',
                    first_name=f'Firstname{i}',
                    last_name=f'Lastname{i}'
                )
                print(f'Created {user}')

            print('Done')
        except IntegrityError:
            print('There are already test users in db. Use "drop_users" command to drop them and try again')
