from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns

from .settings import DEBUG

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/auth/', include('social_django.urls', namespace="social")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout')
]

urlpatterns += i18n_patterns(
    url(r'^', include('section.urls', namespace='section')),
    prefix_default_language=False
)

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
