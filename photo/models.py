from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


class Photo(models.Model):
    title = models.CharField(max_length=200)
    memo = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="photo", width_field="width_field", height_field="height_field")
    thumbnail = ImageSpecField(
        source = 'photo',
        processors = [Thumbnail(200, 200)],
        format = 'JPEG',
        options = {'quality': 60}
    )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    photo_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.title

