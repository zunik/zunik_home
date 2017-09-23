from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_id = models.CharField(max_length=255)
    memo = models.TextField(null=True, blank=True)
    video_at = models.DateField()
    video_type = models.CharField(max_length=50, default='youtube')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hide = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_video_url(self):
        if self.video_type == 'youtube':
            return "//www.youtube.com/embed/" + self.video_id + "?rel=0"
        elif self.video_type == 'naver':
            return "//serviceapi.rmcnmv.naver.com/flash/outKeyPlayer.nhn?" + self.video_id + \
                   "&controlBarMovable=true&jsCallable=true&isAutoPlay=true&skinName=tvcast_white"
