from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView
from tagging.views import TaggedObjectList
from .models import Diary


class OpenDiaryYearView(YearArchiveView):
    queryset = Diary.objects.filter(hide=False)
    date_field = 'diary_at'
    make_object_list = True
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryYearView, self).get_context_data(**kwargs)
        context['now_year'] = int(self.get_year())
        context['year_list'] = list(Diary.objects.filter(hide=False).dates('diary_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Diary.objects.filter(diary_at__year=date.year, hide=False).count()
            i = i + 1

        context['list_type'] = 'year'
        return context


class OpenDiaryTagView(TaggedObjectList):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryTagView, self).get_context_data(**kwargs)
        context['year_list'] = list(Diary.objects.filter(hide=False).dates('diary_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Diary.objects.filter(diary_at__year=date.year, hide=False).count()
            i = i + 1

        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class OpenDiaryDetailView(DetailView):
    queryset = Diary.objects.filter(hide=False)


def open_diary_redirect(request):
    last_diary = Diary.objects.filter(hide=False).latest('diary_at')
    year = last_diary.diary_at.year

    return HttpResponseRedirect(reverse('diary:open_list_year', args=(year,)))