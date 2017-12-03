from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from tagging.fields import TagField
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from hitcount.models import HitCount
from zunik_home.settings import SITE_DOMAIN


def file_rename(instance, filename):
    return "photo/{}" . format(filename)


def file_rename_other(instance, filename):
    return "photo/other/{}" . format(filename)


class Photo(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    memo = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to=file_rename, width_field="width_field", height_field="height_field")
    thumbnail = ImageSpecField(
        source = 'photo',
        processors = [Thumbnail(250, 250)],
        format = 'JPEG',
        options = {'quality': 60}
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    photo_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    tag = TagField()
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    class Meta:
        ordering = ['-photo_at', '-id']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('photo:my_detail', args=[str(self.id)])

    def get_full_absolute_url(self):
        return SITE_DOMAIN + reverse('photo:my_detail', args=[str(self.id)])

    def get_id_string_format(self):
        return str(self.id)


class OtherPhoto(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=file_rename_other, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
