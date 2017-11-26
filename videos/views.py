from django.views.generic import DetailView, ListView
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem, Tag
from .models import Video
from zunik_home.help import custom_paginator


class MyVideoListView(ListView):
    queryset = Video.objects.filter(hide=False)
    paginate_by = 15
    template_name = 'videos/video_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyVideoListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context


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

        relation_num = 8
        context['related_list'] = TaggedItem.objects.get_related(context['object'], Video, relation_num)

        relation_plus_count = relation_num - len(context['related_list'])

        # tags 관련 영상을 뽑아도 개수에 충족하지 못 한다면 최근거에서 부족한 만큼 가져오기
        if relation_plus_count != 0:
            context['related_list'].extend(Video.objects.exclude(pk=context['object'].id).all()[:relation_plus_count])

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

        context['next_object'] = objects.filter(hide=False).filter(video_at__gte=context['object'].video_at)\
            .exclude(video_at=context['object'].video_at, id__lte=context['object'].id).order_by('-video_at', '-id')\
            .last()

        context['prev_object'] = objects.filter(hide=False).filter(video_at__lte=context['object'].video_at) \
            .exclude(video_at=context['object'].video_at, id__gte=context['object'].id).order_by('-video_at', '-id')\
            .first()

        return context

