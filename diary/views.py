from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic.dates import YearArchiveView
from django.views.generic import DetailView
from tagging.views import TaggedObjectList
from .models import Diary


class DiaryYearView(YearArchiveView):
    model = Diary
    date_field = 'diary_at'
    make_object_list = True
    paginate_by = 15
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(DiaryYearView, self).get_context_data(**kwargs)
        context['now_year'] = int(self.get_year())
        context['year_list'] = list(Diary.objects.dates('diary_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Diary.objects.filter(diary_at__year = date.year).count()

        context['list_type'] = 'year'
        return context


class DiaryTagView(TaggedObjectList):
    model = Diary
    paginate_by = 15
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(DiaryTagView, self).get_context_data(**kwargs)
        context['year_list'] = list(Diary.objects.dates('diary_at', 'year', order='DESC'))

        i = 0
        for date in context['year_list']:
            year = context['year_list'][i].year
            context['year_list'][i] = {}
            context['year_list'][i]['year'] = year
            context['year_list'][i]['count'] = Diary.objects.filter(diary_at__year=date.year).count()
            i = i + 1

        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class DiaryDetailView(DetailView):
    model = Diary


def my_diary_redirect(request):
    last_diary = Diary.objects.latest('diary_at')
    year = last_diary.diary_at.year

    return HttpResponseRedirect(reverse('diary:list_year', args=(year,)))