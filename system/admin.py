from django.contrib import admin
from system.models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Inscription)
admin.site.register(SpeechType)
admin.site.register(Topic)
admin.site.register(DateState)


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'published', 'days', 'places')

    list_editable = ('published','days', 'places')


@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    list_display = ('style','user', 'amount', 'size')
    list_display_links = ('style',)
    list_editable = ('amount', 'size')


@admin.register(TshirtStyle)
class TshirtStyleAdmin(admin.ModelAdmin):
    list_display = ('name','description', 'img1', 'img2', 'img3',)
    list_editable = ('description', 'img1', 'img2', 'img3',)
    list_display_links = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer','created','published')

    list_editable = ('published',)

