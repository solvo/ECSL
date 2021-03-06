from django.contrib import admin
from system.models import *
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
# Register your models here.
admin.site.register(DateState)
admin.site.register(Room)
admin.site.register(Hotel)
admin.site.register(QuestionCategory)
admin.site.register(SpeechResource)


@admin.register(Speech)
class SpeechAdmin(admin.ModelAdmin):
    list_display = ('topic', 'user', 'published', 'activity_start', 'places')
    list_editable = ('published','activity_start', 'places')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name', 'description',)


@admin.register(SpeechType)
class SpeechTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ('name',)


@admin.register(Tshirt)
class TshirtAdmin(admin.ModelAdmin):
    list_display = ('style','user', 'amount', 'size', 'payed', 'gender')
    list_display_links = ('style',)
    list_editable = ('amount', 'size', 'payed', 'gender')


@admin.register(TshirtStyle)
class TshirtStyleAdmin(admin.ModelAdmin):
     list_display = ('name', 'img1', 'img2', 'img3',)
     list_editable = ('img1', 'img2', 'img3',)
     list_display_links = ('name',)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('category', 'question', 'answer','created','published')
    list_editable = ('published',)


@admin.register(Patrocinadores)
class PatrocinadoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'web', 'logo',)


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subvention_request', 'registered', 'not_registered')
    list_editable = ('registered', 'not_registered')
    actions = ['send_email_aprove', 'send_email_denieg']

    def send_email_aprove(self, request, queryset):
        for date in queryset:
            send_mail('Hola','Ustaed ha sido aprobado', 'chicomtz.sr@gmail.com',[date.user.email])
        queryset.update(registered=True)
        rows_updated = queryset.update(not_registered=False)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)

    send_email_aprove.short_description = 'Enviar correo de aprobado'

    def send_email_denieg(self, request, queryset):

        for date in queryset:

          send_mail('Hola','Ha sido denegado', 'chicomtz.sr@gmail.com',[date.user.email])

        queryset.update(not_registered=True)
        rows_updated = queryset.update(registered=False)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)

    send_email_denieg.short_description = 'Enviar correo de no aprobado'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    actions = ['send_email_invitation', 'send_email_diploma']
    list_display = ['name', 'enrolled', 'invitation_file', 'diploma',]

    def send_email_invitation(self, request, queryset):

        for date in queryset:
            correo = EmailMessage('Bienvenido', 'Este es el cuerpo del mensaje', settings.DEFAULT_FROM_EMAIL,
                                  [date.user.email, ])

            correo.attach(settings.MEDIA_ROOT + '/pdf/invitacion.pdf', 'application/pdf')
            correo.content_subtype = 'html'
            correo.send()

        rows_updated = queryset.update(invitation_file=True)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)

    send_email_invitation.short_description = 'Enviar archivo de invitacion'

    def send_email_diploma(self, request, queryset):

        for date in queryset:
            correo = EmailMessage('Gracias por asistir', 'Este es el cuerpo del mensaje', settings.DEFAULT_FROM_EMAIL,
                                  [date.user.email, ])

            correo.attach(settings.MEDIA_ROOT + '/pdf/diploma.pdf', 'application/pdf')
            correo.content_subtype = 'html'
            correo.send()

        rows_updated = queryset.update(diploma=True)

        if rows_updated == 1:
            message_bit = "1 email was sent"
        else:
            message_bit = "%s emails were sent" % rows_updated
        self.message_user(request, "%s successfully" % message_bit)

    send_email_diploma.short_description = 'Enviar archivo de diploma'
