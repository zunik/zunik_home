from django.contrib import admin
from django.db import models
from .models import Photo, OtherPhoto

from pagedown.widgets import AdminPagedownWidget


class PhotoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    search_fields = ['title']


class OtherPhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'photo', 'created_at']
    search_fields = ['title', 'photo']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(OtherPhoto, OtherPhotoAdmin)
