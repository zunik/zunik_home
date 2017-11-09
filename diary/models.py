from django.db import models
from tagging.fields import TagField
from django.urls import reverse


class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    diary_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)
    tag = TagField()

    class Meta:
        ordering = ['-diary_at']

    def __str__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('diary:open_detail', args=[str(self.id)])

    def get_id_string_format(self):
        return str(self.id)