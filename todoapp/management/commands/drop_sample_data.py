from django.core.management.base import BaseCommand

from todoapp.models import Project


class Command(BaseCommand):
    help = 'Drop all projects and todos in database'

    def handle(self, *args, **options):
        Project.objects.all().delete()
        print('Dropped all projects and todos')
