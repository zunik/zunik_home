from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from tagging.fields import TagField
from django.urls import reverse


class Photo(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="photo", width_field="width_field", height_field="height_field")
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

    class Meta:
        ordering = ['-photo_at', '-id']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('photo:my_detail', args=[str(self.id)])

    def get_id_string_format(self):
        return str(self.id)