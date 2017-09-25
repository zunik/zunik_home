from django.shortcuts import render, HttpResponseRedirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView
from django.db.models import Q
from .models import Video


class MyVideoYearView(YearArchiveView):
    model = Video
    date_field = 'video_at'
    make_object_list = True
    paginate_by = 12

    def get_context_data(self, **kwargs):
        contact = super(MyVideoYearView, self).get_context_data(**kwargs)
        contact['now_year'] = self.get_year()
        contact['year_list'] = Video.objects.dates('video_at', 'year', order='DESC')
        return contact


class MyVideoDetailView(DetailView):
    model = Video


def my_video_redirect(request):
    last_video = Video.objects.latest('video_at')
    year = last_video.video_at.year

    return HttpResponseRedirect(reverse('video:list_year', args=(year,)))

