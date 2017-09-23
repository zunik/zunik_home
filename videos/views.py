from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.dates import YearArchiveView
from django.db.models import Q
from .models import Video


class MyVideoYearView(YearArchiveView):
    model = Video
    date_field = 'video_at'
    make_object_list = True

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
