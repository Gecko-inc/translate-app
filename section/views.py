import subprocess
import os
import time

from django.conf import settings
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
        file_name = f'{str(time.time()).replace(".", "")}.wav'
        file_name_out = f'{str(time.time()).replace(".", "1")}.wav'

        with open(file_name, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        process = subprocess.run(['ffmpeg', '-i', file_name, file_name_out])
        if process.returncode != 0:
            raise Exception("Что-то пошло не так")
        rec = sr.Recognizer()
        sample_audio = sr.AudioFile(file_name_out)
        with sample_audio as audio_file:
            audio_content = rec.record(audio_file)
            txt = rec.recognize_google(audio_content, language="ru-RU")
        os.remove(file_name)
        os.remove(file_name_out)
        print(txt)
        return JsonResponse({"msg": txt})
