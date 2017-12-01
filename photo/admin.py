from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Photo, PhotoAdmin)