from django.urls import path
from .views import Index
from django.views.decorators.csrf import csrf_exempt

app_name = "section"

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('trans/', csrf_exempt(Index.translate_audio), name='trans')
]
