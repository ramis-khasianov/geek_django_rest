# Generated by Django 3.1 on 2021-08-29 11:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='member',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
