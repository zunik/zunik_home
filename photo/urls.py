from django.conf.urls import url
from . import views

app_name = 'photo'
urlpatterns = [
    url(r'^my/$', views.MyPhotoListView.as_view(), name='my_list'),
    url(r'^my/tag/(?P<tag>[^/]+(?u))/$',views.MyPhotoTagView.as_view(), name='my_list_tag'),
    url(r'^my/(?P<pk>[0-9]+)/$', views.MyPhotoDetailView.as_view(), name='my_detail'),
]