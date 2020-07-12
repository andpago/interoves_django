# Generated by Django 2.1.5 on 2020-07-11 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_remove_taskgroup_rules'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='rules',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='games.HTMLPage'),
        ),
        migrations.AddField(
            model_name='taskgroup',
            name='rules',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_groups', to='games.HTMLPage'),
        ),
    ]