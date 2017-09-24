from django.conf.urls import url
from . import views

app_name = 'photo'
urlpatterns = [
    url(r'^$', views.my_photo_redirect, name='list'),
    url(r'^(?P<year>\d{4})/$',views.MyPhotoYearView.as_view(), name='list_year'),
    url(r'^(?P<pk>[0-9]+)/$', views.MyPhotoDetailView.as_view(), name='detail_view'),
]