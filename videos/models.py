from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=255)
    memo = models.TextField(null=True, blank=True)
    video_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_video_url(self):
        return "//www.youtube.com/embed/" + self.video_id + "?rel=0"

    def get_video_thumbnail(self):
        return "//img.youtube.com/vi/" + self.video_id + "/hqdefault.jpg"
