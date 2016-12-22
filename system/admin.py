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
    list_display = ('topic', 'user', 'published', 'days', 'places')

    list_editable = ('published','days', 'places')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer','created','published')

    list_editable = ('published',)

