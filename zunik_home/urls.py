from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^video/', include('videos.urls')),
    url(r'^photo/', include('photo.urls')),
    url(r'^diary/', include('diary.urls')),

    url(r'^robots\.txt$', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
