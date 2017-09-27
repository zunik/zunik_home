from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_filter = ['video_at']
    search_fields = ['title']

admin.site.register(Video, VideoAdmin)