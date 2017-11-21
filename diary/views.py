from django.views.generic import DetailView, ListView
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem
from .models import Diary
from zunik_home.help import custom_paginator


class OpenDiaryListView(ListView):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context


class OpenDiaryTagView(TaggedObjectList):
    model = Diary
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryTagView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)
        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class OpenDiaryDetailView(DetailView):
    queryset = Diary.objects.filter(hide=False)

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryDetailView, self).get_context_data(**kwargs)
        object_path = '/diary/open/' + str(context['object'].id) + '/';
        context['mentioned_list'] = Diary.objects.filter(content__icontains=object_path)

        relation_num = 5
        context['related_list'] = TaggedItem.objects.get_related(context['object'], Diary, relation_num)

        context['next_object'] = Diary.objects.filter(diary_at__gte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__lte=context['object'].id).order_by('-diary_at','-id').last()

        context['prev_object'] = Diary.objects.filter(diary_at__lte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__gte=context['object'].id).order_by('-diary_at', '-id').first()

        return context
