from django.views.generic import DetailView, ListView
from django.db.models import Q
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem, Tag
from .models import Video, FavoriteVideo
from zunik_home.help import custom_paginator
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class MyVideoListView(ListView):
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyVideoListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context

    def get_queryset(self):
        queryset_list = Video.objects.filter(hide=False)

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(Q(title__icontains=query)).distinct()

        return queryset_list


class MyVideoTagView(TaggedObjectList):
    model = Video
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyVideoTagView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)
        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class MyVideoDetailView(DetailView):
    queryset = Video.objects.filter(hide=False)

    def get_context_data(self, **kwargs):
        context = super(MyVideoDetailView, self).get_context_data(**kwargs)

        # 조회수
        hit_count = HitCount.objects.get_for_object(context['object'])
        HitCountMixin.hit_count(self.request, hit_count)

        relation_num = 8
        context['related_list'] = TaggedItem.objects.get_related(context['object'], self.queryset, relation_num)

        relation_plus_count = relation_num - len(context['related_list'])

        # tags 관련 영상을 뽑아도 개수에 충족하지 못 한다면 최근거에서 부족한 만큼 가져오기
        if relation_plus_count != 0:
            context['related_list'].extend(Video.objects.filter(hide=False).exclude(pk=context['object'].id).all()[:relation_plus_count])

        context['related_list'] = list(set(context['related_list']))

        # 목록으로 돌아갈시 page
        now_page = self.request.GET.get('page')
        if not now_page:
            now_page = 1
        context['now_page'] = now_page

        # 다음 글 , 이전 글
        now_tag = self.request.GET.get('tag')

        if now_tag:
            tag_object = Tag.objects.get(name=now_tag)
            objects = TaggedItem.objects.get_by_model(Video, tag_object)
            context['now_tag'] = now_tag
        else:
            objects = Video.objects

            query = self.request.GET.get('q')
            if query:
                objects = objects.filter(Q(title__icontains=query)).distinct()

        objects = objects.filter(hide=False)

        context['next_object'] = objects.filter(video_at__gte=context['object'].video_at) \
            .exclude(video_at=context['object'].video_at, id__lte=context['object'].id).order_by('-video_at', '-id') \
            .last()

        context['prev_object'] = objects.filter(video_at__lte=context['object'].video_at) \
            .exclude(video_at=context['object'].video_at, id__gte=context['object'].id).order_by('-video_at', '-id') \
            .first()

        return context


class FavoriteVideoListView(ListView):
    queryset = FavoriteVideo.objects.filter(hide=False)
    paginate_by = 15
    template_name = 'videos/favorite_video_list.html'

    def get_context_data(self, **kwargs):
        context = super(FavoriteVideoListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context


class FavoriteVideoTagView(TaggedObjectList):
    model = FavoriteVideo
    paginate_by = 15
    template_name = 'videos/favorite_video_list.html'

    def get_context_data(self, **kwargs):
        context = super(FavoriteVideoTagView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)
        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class FavoriteVideoDetailView(DetailView):
    queryset = FavoriteVideo.objects.filter(hide=False)
    template_name = 'videos/favorite_video_detail.html'

    def get_context_data(self, **kwargs):
        context = super(FavoriteVideoDetailView, self).get_context_data(**kwargs)

        # 조회수
        hit_count = HitCount.objects.get_for_object(context['object'])
        HitCountMixin.hit_count(self.request, hit_count)

        relation_num = 8
        context['related_list'] = TaggedItem.objects.get_related(context['object'], self.queryset, relation_num)

        relation_plus_count = relation_num - len(context['related_list'])

        # tags 관련 영상을 뽑아도 개수에 충족하지 못 한다면 최근거에서 부족한 만큼 가져오기
        if relation_plus_count != 0:
            context['related_list'].extend(FavoriteVideo.objects.filter(hide=False).exclude(pk=context['object'].id).all()[:relation_plus_count])

        context['related_list'] = list(set(context['related_list']))

        # 목록으로 돌아갈시 page
        now_page = self.request.GET.get('page')
        if not now_page:
            now_page = 1
        context['now_page'] = now_page

        # 다음 글 , 이전 글
        now_tag = self.request.GET.get('tag')

        if now_tag:
            tag_object = Tag.objects.get(name=now_tag)
            objects = TaggedItem.objects.get_by_model(FavoriteVideo, tag_object)
            context['now_tag'] = now_tag
        else:
            objects = FavoriteVideo.objects

        context['next_object'] = objects.filter(hide=False).filter(id__gt=context['object'].id).last()

        context['prev_object'] = objects.filter(hide=False).filter(id__lt=context['object'].id).first()

        return context

