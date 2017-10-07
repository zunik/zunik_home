from django.conf.urls import url
from . import views

app_name = 'diary'
urlpatterns =[
    url(r'^(?P<pk>[0-9]+)/$', views.DiaryDetailView.as_view(), name='detail_view'),
]