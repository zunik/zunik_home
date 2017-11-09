from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem
from .models import Video


class MyVideoYearView(YearArchiveView):
    model = Video
    date_field = 'video_at'
    make_object_list = True
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyVideoYearView, self).get_context_data(**kwargs)
        context['now_year'] = int(self.get_year())
        context['year_list'] = list(Video.objects.dates('video_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Video.objects.filter(video_at__year = date.year).count()
            i = i + 1

        context['list_type'] = 'year'
        return context


class MyVideoTagView(TaggedObjectList):
    model = Video
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyVideoTagView, self).get_context_data(**kwargs)
        context['year_list'] = list(Video.objects.dates('video_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Video.objects.filter(video_at__year=date.year).count()
            i = i + 1

        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class MyVideoDetailView(DetailView):
    model = Video

    def get_context_data(self, **kwargs):
        # 총 next_video 에 뽑아서 보여줄 개수
        next_video_num = 8
        context = super(MyVideoDetailView, self).get_context_data(**kwargs)
        context['next_video_list'] = TaggedItem.objects.get_related(context['object'], self.model, next_video_num)

        next_video_plus_count = next_video_num - len(context['next_video_list'])

        # tags 관련 영상을 뽑아도 개수에 충족하지 못 한다면 최근거에서 부족한 만큼 가져오기
        if next_video_plus_count != 0:
            context['next_video_list'].extend(self.model.objects.exclude(pk=context['object'].id)
                                              .all()[:next_video_plus_count])
        return context


def my_video_redirect(request):
    last_video = Video.objects.latest('video_at')
    year = last_video.video_at.year

    return HttpResponseRedirect(reverse('video:my_list_year', args=(year,)))

