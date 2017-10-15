from django.contrib import admin
from django.db import models
from .models import Diary

from pagedown.widgets import AdminPagedownWidget


class DiaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    list_filter = ['diary_at']
    search_fields = ['title', 'content']
    list_display = ['title', 'diary_at', 'hide']

admin.site.register(Diary, DiaryAdmin)
