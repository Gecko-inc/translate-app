import subprocess
import time
import threading

from django.core.files import File
from gtts import gTTS
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
import speech_recognition as sr
from deep_translator import GoogleTranslator
from config.views import common_context, delete_file
from section.models import Audio


class Index(TemplateView):
    template_name = 'page/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update(common_context())

        return context

    @classmethod
    def translate_audio(cls, request):
        # TODO: Нужно оптимизировать
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

            ru_text = GoogleTranslator(source='auto', target='ru').translate(text=txt)
            eng_text = GoogleTranslator(source='auto', target='en').translate(text=txt)
            kz_text = GoogleTranslator(source='auto', target='kk').translate(text=txt)
            ru_obj = gTTS(text=ru_text, lang='ru', slow=False)
            ru_name = f"ru_file{str(time.time()).replace('.', '')}.mp3"
            ru_obj.save(ru_name)

            en_obj = gTTS(text=eng_text, lang='en', slow=False)
            en_name = f"en_file{str(time.time()).replace('.', '')}.mp3"
            en_obj.save(en_name)

            kz_obj = gTTS(text=kz_text, lang='ru', slow=False)
            kz_name = f"kz_file{str(time.time()).replace('.', '')}.mp3"
            kz_obj.save(kz_name)
            audio = Audio.objects.create(
                kz_audio=File(file=open(kz_name, 'rb'), name=kz_name),
                ru_audio=File(file=open(ru_name, 'rb'), name=ru_name),
                eng_audio=File(file=open(en_name, 'rb'), name=en_name),
            )
            threading.Thread(target=delete_file, name='delete_files',
                             args=([kz_name, en_name, ru_name, file_name, file_name_out],)).start()

            return render(request, "page/result.html", {"ru_text": ru_text,
                                                        "eng_text": eng_text,
                                                        "kz_text": kz_text,
                                                        "audio": audio,
                                                        })

        return JsonResponse({
            "msg": "error"
        })
