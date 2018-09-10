from django.conf.urls import url
from . import views

app_name = 'video'
urlpatterns = [
    url(r'^my/$', views.MyVideoListView.as_view(), name='my_list'),
    url(r'^my/tag/(?P<tag>[^/]+(?u))/$', views.MyVideoTagView.as_view(), name='my_list_tag'),
    url(r'^my/(?P<pk>[0-9]+)/$', views.MyVideoDetailView.as_view(), name='my_detail'),
    url(r'^favorite/$', views.FavoriteVideoListView.as_view(), name='favorite_list'),
    url(r'^favorite/tag/(?P<tag>[^/]+(?u))/$', views.FavoriteVideoTagView.as_view(), name='favorite_list_tag'),
    url(r'^favorite/(?P<pk>[0-9]+)/$', views.FavoriteVideoDetailView.as_view(), name='favorite_detail'),
]