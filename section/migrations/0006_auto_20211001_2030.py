# Generated by Django 3.1.6 on 2021-10-01 17:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0005_auto_20210929_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='create',
        ),
        migrations.AddField(
            model_name='audio',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]