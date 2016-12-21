from _csv import list_dialects

from django.contrib import admin
from system.models import *
# Register your models here.
admin.site.register(TshirtStyle)
admin.site.register(Tshirt)
admin.site.register(Profile)
admin.site.register(Inscription)
admin.site.register(SpeechType)
admin.site.register(Topic)
admin.site.register(DateState)


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'audience', 'published')
    #list_display_links = ('published',)
    list_editable = ('published',)

