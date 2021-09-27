from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserStatus(models.Model):
    title = models.CharField(_("Название"), max_length=130)

    class Meta:
        verbose_name = _("Статус пользователя")
        verbose_name_plural = _("Статусы пользователей")

    def __str__(self):
        return self.title


class User(AbstractUser, UserManager):
    status = models.ForeignKey(UserStatus, verbose_name=_("Статус"), on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self):
        return self.username + " | " + str(self.status)
