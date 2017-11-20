from django.views.generic import DetailView, ListView
from tagging.views import TaggedObjectList
from .models import Diary


class OpenDiaryListView(ListView):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryListView, self).get_context_data(**kwargs)

        paginator = context['paginator']
        page_obj = context['page_obj']
        page_numbers_range = 7;
        max_page = len(paginator.page_range)
        current_page = page_obj.number

        current_page_pack = int((current_page - 1) / page_numbers_range)
        end_page_pack = int((max_page - 1) / page_numbers_range)

        start_page = current_page_pack * page_numbers_range
        end_page = start_page + page_numbers_range

        if end_page >= max_page:
            end_page = max_page

        if current_page_pack == end_page_pack:
            has_next_pack = False
        else:
            has_next_pack = True

        if current_page_pack == 0:
            has_previous_pack = False
        else:
            has_previous_pack = True

        custom_page_obj = {
            'page_range': paginator.page_range[start_page:end_page],
            'start_page' : start_page,
            'end_page' : end_page,
            'has_next_pack' : has_next_pack,
            'has_previous_pack' : has_previous_pack,
        }

        context['custom_page_obj'] = custom_page_obj

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
