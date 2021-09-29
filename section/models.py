import os
import datetime

from django.db import models
from django.utils import timezone

from config.views import get_upload_to


class Audio(models.Model):
    IMAGE_PATH = "sections/audio"

    eng_audio = models.FileField(upload_to=get_upload_to, blank=True, null=True)
    ru_audio = models.FileField(upload_to=get_upload_to, blank=True, null=True)
    kz_audio = models.FileField(upload_to=get_upload_to, blank=True, null=True)

    create = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Аудиофайл"
        verbose_name_plural = "Аудиофайлы"

    def __str__(self):
        return f"#{self.id}"

    @classmethod
    def delete_old(cls):
        delete_date = datetime.datetime.now() - datetime.timedelta(days=1)
        for item in cls.objects.filter(create__lte=delete_date):
            os.remove(item.eng_audio.url)
            os.remove(item.ru_audio.url)
            os.remove(item.kz_audio.url)
            item.delete()
