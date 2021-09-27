import os
import time

from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.views.generic import TemplateView
import speech_recognition as sr

from config.views import common_context


class Index(TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update(common_context())

        return context

    @classmethod
    def translete_audio(cls, request):
        file = request.FILES['voice']
        file_name = default_storage.save(f"{str(time.time()).replace('.', '')}{file.name}.wav", file)
        file = default_storage.open(file_name)
        print(default_storage.url(file_name))
        rec = sr.Recognizer()
        sample_audio = sr.AudioFile(file)
        with sample_audio as audio_file:
            audio_content = rec.record(audio_file)
            txt = rec.recognize_google(audio_content, language="ru-RU")
            print(txt)
        os.remove(default_storage.url(file_name))
        return JsonResponse({"msg": True})
