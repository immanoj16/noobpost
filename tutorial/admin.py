from django.contrib import admin
from tutorial.models import Tutorial, Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']


class TutorialAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['title']
    filter_horizontal = ('similar', 'videos',)

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Video, VideoAdmin)
