from django.views.generic import DetailView, ListView
from tagging.views import TaggedObjectList
from .models import Diary


class OpenDiaryListView(ListView):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryListView, self).get_context_data(**kwargs)

        context['list_type'] = 'all'
        return context


class OpenDiaryTagView(TaggedObjectList):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryTagView, self).get_context_data(**kwargs)

        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class OpenDiaryDetailView(DetailView):
    queryset = Diary.objects.filter(hide=False)
