from django.conf.urls import url
from . import views

app_name = 'diary'
urlpatterns =[
    url(r'^open/$', views.OpenDiaryListView.as_view(), name='open_list'),
    url(r'^open/tag/(?P<tag>[^/]+(?u))/$', views.OpenDiaryTagView.as_view(), name='open_list_tag'),
    url(r'^open/(?P<pk>[0-9]+)/$', views.OpenDiaryDetailView.as_view(), name='open_detail'),
]