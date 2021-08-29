from django.core.management.base import BaseCommand
from userapp.models import User


class Command(BaseCommand):
    help = 'Drop all users in database'

    def handle(self, *args, **options):
        User.objects.all().delete()
        print('Dropped all users')
