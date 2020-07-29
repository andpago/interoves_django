# Generated by Django 2.1.5 on 2020-07-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0031_auto_20200726_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attempt',
            name='possible_status',
            field=models.CharField(blank=True, choices=[('Ok', 'Ok'), ('Pending', 'Pending'), ('Partial', 'Partial'), ('Wrong', 'Wrong')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='attempt',
            name='status',
            field=models.CharField(choices=[('Ok', 'Ok'), ('Pending', 'Pending'), ('Partial', 'Partial'), ('Wrong', 'Wrong')], max_length=100),
        ),
    ]