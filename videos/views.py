from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView,ListView
from tagging.views import TaggedObjectList
from .models import Video


class MyVideoYearView(YearArchiveView):
    model = Video
    date_field = 'video_at'
    make_object_list = True
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        contact = super(MyVideoYearView, self).get_context_data(**kwargs)
        contact['now_year'] = int(self.get_year())
        contact['year_list'] = Video.objects.dates('video_at', 'year', order='DESC')
        contact['list_type'] = 'year'
        return contact


class MyVideoTagView(TaggedObjectList):
    model = Video
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        contact = super(MyVideoTagView, self).get_context_data(**kwargs)
        contact['year_list'] = Video.objects.dates('video_at', 'year', order='DESC')
        contact['now_tag'] = contact['tag']
        contact['list_type'] = 'tag'
        del(contact['tag'])
        return contact


class MyVideoDetailView(DetailView):
    model = Video


def my_video_redirect(request):
    last_video = Video.objects.latest('video_at')
    year = last_video.video_at.year

    return HttpResponseRedirect(reverse('video:list_year', args=(year,)))

