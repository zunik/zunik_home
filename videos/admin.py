from django.contrib import admin
from django.db import models
from .models import Video, FavoriteVideo

from pagedown.widgets import AdminPagedownWidget


class VideoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_filter = ['video_at']
    search_fields = ['title']


class FavoriteVideoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    search_fields = ['title']

admin.site.register(Video, VideoAdmin)
admin.site.register(FavoriteVideo, FavoriteVideoAdmin)