from django.db import models
from tagging.fields import TagField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from hitcount.models import HitCount
from zunik_home.settings import SITE_DOMAIN


class Diary(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255, default='간략한 내용')
    content = models.TextField()
    diary_at = models.DateField()
    main_img = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    tag = TagField()
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-diary_at', '-id']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('diary:open_detail', args=[str(self.id)])

    def get_full_absolute_url(self):
        return SITE_DOMAIN + reverse('diary:open_detail', args=[str(self.id)])

    def get_id_string_format(self):
        return str(self.id)

    def get_main_img_url(self):
        if self.main_img:
            return SITE_DOMAIN + self.main_img
        else:
            return False
