# Generated by Django 2.1.5 on 2020-07-11 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_task_task_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='rules',
        ),
    ]