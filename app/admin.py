from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('comment', 'image', 'tags', 'user')
    # list_display_links = ('id', 'title')


admin.site.register(Photo, PhotoAdmin)
