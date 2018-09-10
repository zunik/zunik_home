from django.shortcuts import render
from diary.models import Diary
from videos.models import Video


def index(request):
    diarys = Diary.objects.filter(recommend=True).order_by('?')[:6]
    videos = Video.objects.filter(recommend=True).order_by('?')[:4]

    context = {
        'diarys': diarys,
        'videos': videos,
    }
    return render(request, 'main.html', context)
