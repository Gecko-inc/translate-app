from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _

from config.views import get_upload_to


class Section(models.Model):
    IMAGE_PATH = "sections/section"

    title = models.CharField(_("Заголовок"), max_length=130)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=True)
    slug = models.CharField(_("URL адрес"), max_length=130, help_text=_("Заполняется автоматически"))
    description = models.TextField(_("Описание"), max_length=500, blank=True)
    show_main = models.BooleanField(_("Отображать на главной?"), default=False)
    is_active = models.BooleanField(_("Активна"), default=False)

    class Meta:
        verbose_name = _("Раздел")
        verbose_name_plural = _("Разделы")

    def __str__(self):
        return self.title


class Article(models.Model):
    IMAGE_PATH = "sections/article"

    title = models.CharField(_("Заголовок"), max_length=130)
    slug = models.CharField(_("URL адрес"), max_length=130, help_text=_("Заполняется автоматически"))
    section = models.ForeignKey(Section, verbose_name=_("Раздел"), on_delete=models.SET_NULL, null=True,
                                related_name="articles", blank=True)
    short_description = models.TextField(_("Краткое описание"), max_length=500, blank=True)
    text = RichTextUploadingField(_('Текст публикации'), blank=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to, blank=True)
    is_active = models.BooleanField(_("Активна"), default=False)

    class Meta:
        verbose_name = _("Статья")
        verbose_name_plural = _("Статьи")

    def __str__(self):
        return self.title


class ArticleMedia(models.Model):
    article = models.ForeignKey(Article, verbose_name=_("Статья"), on_delete=models.CASCADE)
    title = models.CharField(_("Заголовок"), max_length=130, blank=True)
    image = models.ImageField(_("Изображение"), upload_to=get_upload_to)
