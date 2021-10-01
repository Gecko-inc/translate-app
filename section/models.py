import os
import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware


class Audio(models.Model):
    eng_audio = models.FileField(upload_to='audio', blank=True, null=True)
    ru_audio = models.FileField(upload_to='audio', blank=True, null=True)
    kz_audio = models.FileField(upload_to='audio', blank=True, null=True)

    date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Аудиофайл"
        verbose_name_plural = "Аудиофайлы"

    def __str__(self):
        return f"#{self.id}"

    @classmethod
    def delete_old(cls):
        delete_date = datetime.datetime.now() - datetime.timedelta(minutes=21)
        for item in cls.objects.filter(date__lte=make_aware(delete_date)):
            if item.eng_audio:
                try:
                    os.remove(f"{settings.MEDIA_ROOT}{item.eng_audio}")
                except FileNotFoundError:
                    pass
            if item.ru_audio:
                try:
                    os.remove(f"{settings.MEDIA_ROOT}{item.ru_audio}")
                except FileNotFoundError:
                    pass
            if item.kz_audio:
                try:
                    os.remove(f"{settings.MEDIA_ROOT}{item.kz_audio}")
                except FileNotFoundError:
                    pass
            item.delete()
