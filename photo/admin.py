from django.contrib import admin
from django.db import models
from .models import Photo, OtherPhoto

from pagedown.widgets import AdminPagedownWidget


class PhotoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    search_fields = ['title']

admin.site.register(Photo, PhotoAdmin)
admin.site.register(OtherPhoto)
