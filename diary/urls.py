from django.conf.urls import url
from . import views

app_name = 'diary'
urlpatterns =[
    url(r'^$', views.my_diary_redirect, name='list'),
    url(r'^year/(?P<year>\d{4})/$', views.DiaryYearView.as_view(), name='list_year'),
    url(r'^(?P<pk>[0-9]+)/$', views.DiaryDetailView.as_view(), name='detail_view'),
    url(r'^tag/(?P<tag>[^/]+(?u))/$', views.DiaryTagView.as_view(), name='list_tag'),
]