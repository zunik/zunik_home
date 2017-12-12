from django.db import models
from tagging.fields import TagField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from hitcount.models import HitCount
from zunik_home.settings import SITE_DOMAIN


class Video(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=255)
    memo = models.TextField(null=True, blank=True)
    video_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    recommend = models.BooleanField(default=False)
    tag = TagField()
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-video_at', '-id']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('video:my_detail', args=[str(self.id)])

    def get_full_absolute_url(self):
        return SITE_DOMAIN + reverse('video:my_detail', args=[str(self.id)])

    def get_video_url(self):
        return "//www.youtube.com/embed/" + self.video_id + "?rel=0"

    def get_video_thumbnail(self):
        return "//img.youtube.com/vi/" + self.video_id + "/hqdefault.jpg"

    def get_id_string_format(self):
        return str(self.id)


class FavoriteVideo(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=200)
    memo = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    tag = TagField()
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('video:favorite_detail', args=[str(self.id)])

    def get_full_absolute_url(self):
        return SITE_DOMAIN + reverse('video:favorite_detail', args=[str(self.id)])

    def get_video_url(self):
        return "//www.youtube.com/embed/" + self.video_id + "?rel=0"

    def get_video_thumbnail(self):
        return "//img.youtube.com/vi/" + self.video_id + "/hqdefault.jpg"

    def get_id_string_format(self):
        return str(self.id)