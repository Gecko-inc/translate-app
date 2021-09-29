import os
import datetime

from django.db import models
from django.utils import timezone


class Audio(models.Model):
    eng_audio = models.FileField(upload_to='audio', blank=True, null=True)
    ru_audio = models.FileField(upload_to='audio', blank=True, null=True)
    kz_audio = models.FileField(upload_to='audio', blank=True, null=True)

    create = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = "Аудиофайл"
        verbose_name_plural = "Аудиофайлы"

    def __str__(self):
        return f"#{self.id}"

    @classmethod
    def delete_old(cls):
        delete_date = datetime.datetime.now() - datetime.timedelta(minutes=21)
        for item in cls.objects.filter(create__lte=delete_date):
            if item.eng_audio:
                try:
                    os.remove(item.eng_audio.url)
                except FileNotFoundError:
                    pass
            if item.ru_audio:
                try:
                    os.remove(item.ru_audio.url)
                except FileNotFoundError:
                    pass
            if item.kz_audio:
                try:
                    os.remove(item.kz_audio.url)
                except FileNotFoundError:
                    pass
            item.delete()
