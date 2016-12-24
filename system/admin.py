from django.contrib import admin
from system.models import *
from django.core.mail import send_mail
# Register your models here.
admin.site.register(Profile)
admin.site.register(SpeechType)
admin.site.register(Topic)
admin.site.register(DateState)
admin.site.register(Patrocinadores)


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'published', 'days', 'places')

    list_editable = ('published','days', 'places')


@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    list_display = ('style','user', 'amount', 'size')
    list_display_links = ('style',)
    list_editable = ('amount', 'size')


# @admin.register(TshirtStyle)
# class TshirtStyleAdmin(admin.ModelAdmin):
#     list_display = ('name','description', 'img1', 'img2', 'img3',)
#     list_editable = ('description', 'img1', 'img2', 'img3',)
#     list_display_links = ('name',)



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer','created','published')
    list_editable = ('published',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('mozilla_subvention_description', 'subvention_description', 'mozilla_subvention', )
    list_editable = ('mozilla_subvention',)
    list_display_links = ('mozilla_subvention_description',)
    actions = ['test']

    def test(self, request, queryset):

        #
        # print(queryset[0].user.username)
        for date in queryset:
          send_mail('Hola','texto del mensanje', 'chicomtz.sr@gmail.com',[date.user.email])

        # rows_updated = queryset.update(mozilla_subvention=True)
        #
        # if rows_updated == 1:
        #     message_bit = "1 story was"
        # else:
        #     message_bit = "%s stories were" % rows_updated
        # self.message_user(request, "%s successfully marked as published." % message_bit)

    test.short_description = 'Email'
