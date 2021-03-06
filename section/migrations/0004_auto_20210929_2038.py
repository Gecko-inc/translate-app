# Generated by Django 3.1.6 on 2021-09-29 17:38

import config.views
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0003_section_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_audio', models.FileField(blank=True, null=True, upload_to=config.views.get_upload_to)),
                ('ru_audio', models.FileField(blank=True, null=True, upload_to=config.views.get_upload_to)),
                ('kz_audio', models.FileField(blank=True, null=True, upload_to=config.views.get_upload_to)),
                ('create', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'Аудиофайл',
                'verbose_name_plural': 'Аудиофайлы',
            },
        ),
        migrations.RemoveField(
            model_name='articlemedia',
            name='article',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='ArticleMedia',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
