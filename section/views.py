import subprocess
import os
import time
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import speech_recognition as sr
from deep_translator import GoogleTranslator
from config.views import common_context


class Index(TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update(common_context())

        return context

    @classmethod
    def translate_audio(cls, request):
        file = request.FILES.get("voice")
        if file:
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
                try:
                    txt = rec.recognize_google(audio_content, language="ru-RU")
                except sr.UnknownValueError:
                    txt = rec.recognize_google(audio_content)
            os.remove(file_name)
            os.remove(file_name_out)
            ru_text = GoogleTranslator(source='auto', target='ru').translate(text=txt)
            eng_text = GoogleTranslator(source='auto', target='en').translate(text=txt)
            kz_text = GoogleTranslator(source='auto', target='kk').translate(text=txt)
            return render(request, "page/result.html", {"ru_text": ru_text,
                                                        "eng_text": eng_text,
                                                        "kz_text": kz_text,
                                                        })

        return JsonResponse({
            "msg": "error"
        })
