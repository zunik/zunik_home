from django.views.generic import DetailView, ListView
from django.contrib.syndication.views import Feed
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem, Tag
from .models import Diary
from zunik_home.help import custom_paginator
from zunik_home.settings import SITE_DOMAIN
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class OpenDiaryListView(ListView):
    queryset = Diary.objects.filter(hide=False)
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context


class OpenDiaryTagView(TaggedObjectList):
    queryset = Diary.objects.filter(hide=False)
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

        # 조회수
        hit_count = HitCount.objects.get_for_object(context['object'])
        HitCountMixin.hit_count(self.request, hit_count)

        object_path = '/diary/open/' + str(context['object'].id) + '/';
        context['mentioned_list'] = Diary.objects.filter(content__icontains=object_path)

        relation_num = 5
        context['related_list'] = TaggedItem.objects.get_related(context['object'], Diary, relation_num)

        # 목록으로 돌아갈시 page
        now_page = self.request.GET.get('page')
        if not now_page:
            now_page = 1
        context['now_page'] = now_page

        # 다음 글, 이전 글
        now_tag = self.request.GET.get('tag')

        if now_tag:
            tag_object = Tag.objects.get(name=now_tag)
            objects = TaggedItem.objects.get_by_model(Diary, tag_object)
            context['now_tag'] = now_tag
        else:
            objects = Diary.objects

        context['next_object'] = objects.filter(hide=False).filter(diary_at__gte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__lte=context['object'].id).order_by('-diary_at', '-id').last()

        context['prev_object'] = objects.filter(hide=False).filter(diary_at__lte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__gte=context['object'].id).order_by('-diary_at', '-id').first()

        return context


class LatestOpenDiaryFeed(Feed):
    title = "주훈이의 오픈 다이어리 입니다."
    description = "최근 5개의 다이어리"
    link = SITE_DOMAIN + "/diary/open/"

    def items(self):
        return Diary.objects.filter(hide=False)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return SITE_DOMAIN + item.get_absolute_url
