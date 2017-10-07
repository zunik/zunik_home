from django.db import models
from tagging.fields import TagField


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