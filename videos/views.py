from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import YearArchiveView
from django.db.models import Q
from .models import Video


class MyVideoYearView(YearArchiveView):
    model = Video
    date_field = 'video_at'
    make_object_list = True
    paginate_by = 5

    def get_context_data(self, **kwargs):
        contact = super(MyVideoYearView, self).get_context_data(**kwargs)
        contact['year_list'] = Video.objects.dates('video_at', 'year', order='DESC')
        return contact


def my_video_redirect(request):
    last_video = Video.objects.latest('video_at')
    year = last_video.video_at.year

    return HttpResponseRedirect(reverse('videos:list_year', args=(year,)))


def my_video_list(request):
    q = request.GET.get('q')
    page = request.GET.get('page')
    queryset = Video.objects

    if q:
        queryset = queryset.filter(Q(title__icontains=q) | Q(memo__icontains=q)).distinct()

    queryset_order = queryset.order_by('-video_at')
    paginator = Paginator(queryset_order, 5)

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    context = {
        'videos': videos,
    }

    return render(request, 'videos/videos_list.html', context)
