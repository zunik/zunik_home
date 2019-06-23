from django.views.generic import DetailView, ListView
from tagging.views import TaggedObjectList
from tagging.models import TaggedItem, Tag
from .models import Photo
from zunik_home.help import custom_paginator
from hitcount.models import HitCount
from hitcount.views import HitCountMixin


class MyPhotoListView(ListView):
    queryset = Photo.objects.filter(hide=False)
    paginate_by = 15
    template_name = 'photo/photo_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyPhotoListView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)

        context['list_type'] = 'all'
        return context


class MyPhotoTagView(TaggedObjectList):
    model = Photo
    paginate_by = 15
    template_name = 'photo/photo_list.html'

    def get_context_data(self, **kwargs):
        context = super(MyPhotoTagView, self).get_context_data(**kwargs)

        context['custom_page_obj'] = custom_paginator(context['paginator'], context['page_obj'], 5)
        context['now_tag'] = context['tag']
        context['list_type'] = 'tag'
        del(context['tag'])
        return context


class MyPhotoDetailView(DetailView):
    queryset = Photo.objects.filter(hide=False)

    def get_context_data(self, **kwargs):
        context = super(MyPhotoDetailView, self).get_context_data(**kwargs)

        # 조회수
        hit_count = HitCount.objects.get_for_object(context['object'])
        HitCountMixin.hit_count(self.request, hit_count)

        relation_num = 8
        context['related_list'] = TaggedItem.objects.get_related(context['object'], self.queryset, relation_num)

        relation_plus_count = relation_num - len(context['related_list'])

        # tags 관련 컨텐츠 뽑아도 개수에 충족하지 못 한다면 최근거에서 부족한 만큼 가져오기
        if relation_plus_count != 0:
            context['related_list'].extend(Photo.objects.filter(hide=False).exclude(pk=context['object'].id).all()[:relation_plus_count])

        # 중복제거
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
            objects = TaggedItem.objects.get_by_model(Photo, tag_object)
            context['now_tag'] = now_tag
        else:
            objects = Photo.objects

        context['next_object'] = objects.filter(hide=False).filter(photo_at__gte=context['object'].photo_at) \
            .exclude(photo_at=context['object'].photo_at, id__lte=context['object'].id).order_by('-photo_at', '-id') \
            .last()

        context['prev_object'] = objects.filter(hide=False).filter(photo_at__lte=context['object'].photo_at) \
            .exclude(photo_at=context['object'].photo_at, id__gte=context['object'].id).order_by('-photo_at', '-id') \
            .first()

        return context
