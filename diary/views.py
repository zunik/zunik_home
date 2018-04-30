from django.views.generic import DetailView, ListView
from django.contrib.syndication.views import Feed
from django.shortcuts import render, get_object_or_404, reverse
from django.db.models import Q
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem, Tag
from .models import Diary
from zunik_home.help import custom_paginator
from zunik_home.settings import SITE_DOMAIN
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class OpenDiaryListView(ListView):
    paginate_by = 10
    template_name = 'diary/diary_list.html'

    def get_context_data(self, **kwargs):
        context = super(OpenDiaryListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context

    def get_queryset(self):
        queryset_list = Diary.objects.filter(hide=False)

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

        return queryset_list


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

        # 이글을 언급한 글
        object_path = '/diary/open/' + str(context['object'].id) + '/';
        context['mentioned_list'] = Diary.objects.filter(hide=False).filter(content__icontains=object_path)

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

            query = self.request.GET.get('q')
            if query:
                objects = objects.filter(
                    Q(title__icontains=query) |
                    Q(content__icontains=query)
                ).distinct()

        objects = objects.filter(hide=False)

        context['next_object'] = objects.filter(diary_at__gte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__lte=context['object'].id).order_by('-diary_at', '-id').last()

        context['prev_object'] = objects.filter(diary_at__lte=context['object'].diary_at)\
            .exclude(diary_at=context['object'].diary_at, id__gte=context['object'].id).order_by('-diary_at', '-id').first()

        # 연관있는 글 (이미 위에서 호출 된것은 제외함)

        filter_list = []

        if context['prev_object']:
            filter_list.append(context['prev_object'].id)

        if context['next_object']:
            filter_list.append(context['next_object'].id)

        if context['mentioned_list']:
            for mentioned in context['mentioned_list']:
                filter_list.append(mentioned.id)

        objects_filter = Diary.objects

        if filter_list:
            for object_id in filter_list:
                objects_filter = objects_filter.filter(~Q(id=object_id))

        relation_num = 5
        context['related_list'] = TaggedItem.objects.get_related(context['object'], objects_filter, relation_num)

        return context


def open_diary_introduction(request):
    query = get_object_or_404(Diary, pk=239)
    full_absolute_url = SITE_DOMAIN + reverse('diary:introduction')

    context = {
        'object': query,
        'full_absolute_url': full_absolute_url,
    }

    # 조회수
    hit_count = HitCount.objects.get_for_object(query)
    HitCountMixin.hit_count(request, hit_count)

    return render(request, 'diary/diary_introduction.html', context)


class LatestOpenDiaryFeed(Feed):
    title = "주훈이의 오픈 다이어리 입니다."
    description = "최근 5개의 다이어리"
    link = SITE_DOMAIN + "/diary/open/"

    def items(self):
        return Diary.objects.filter(hide=False)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return SITE_DOMAIN + item.get_absolute_url

    def item_pubdate(self, item):
        return item.created_at
