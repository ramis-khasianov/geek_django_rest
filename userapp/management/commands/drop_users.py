from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Drop all users in database'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, nargs='?', default=5)

    def handle(self, *args, **options):
        User.objects.all().delete()
        print('Dropped all users')
