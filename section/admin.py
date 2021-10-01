from django.contrib import admin
from .models import Audio


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    pass
