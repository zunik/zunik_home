from django.conf.urls import url
from . import views

app_name = 'video'
urlpatterns =[
    url(r'^$', views.my_video_redirect, name='list'),
    url(r'^(?P<year>\d{4})/$', views.MyVideoYearView.as_view(), name='list_year'),
    url(r'^(?P<pk>[0-9]+)/$', views.MyVideoDetailView.as_view(), name='detail_view'),
]