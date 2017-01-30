# -*- coding: utf-8 -*-
from system.forms import *
from django.shortcuts import render, redirect
from registration.backends.hmac.views import RegistrationView
from registration import signals
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from xhtml2pdf import pisa  # import python module
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.views import logout
from django.conf import settings

@method_decorator(login_required, name='dispatch')
class view_profile(DetailView):
    template_name = 'usuarios/view_profile.html'
    model = Profile


class createProfile(RegistrationView):
    form_class = ProfileForm
    template_name = 'usuarios/create_profile.html'

    def register(self, form):
        formuser = RegistrationForm(data={'username': form.cleaned_data["username"], 'email': form.cleaned_data["email"], 'password1': form.cleaned_data["password1"],
                                          'password2': form.cleaned_data["password2"]})
        new_user = self.create_inactive_user(formuser)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=self.request)
        profile = Profile(name=form.cleaned_data["name"], last_name=form.cleaned_data["last_name"],
                                  gender=form.cleaned_data["gender"], user=new_user,
                                  born_date=form.cleaned_data["born_date"],
                                  nationality=form.cleaned_data["nationality"],
                                  institution=form.cleaned_data["institution"],)
        email_user = [form.cleaned_data['email'], ]
        outputFilename = createPDF(form.cleaned_data["username"])
        correo = EmailMessage('Bienvenido', 'Este es el cuerpo del mensaje', settings.DEFAULT_FROM_EMAIL, [email_user, ])
        correo.attach(outputFilename, 'application/pdf')
        correo.content_subtype = 'html'
        correo.send()

        profile.save()
        return new_user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):


    form_class = EditProfileForm
    template_name = 'usuarios/my_edit_profile.html'
    success_url = "/"
    model = Profile


def createPDF(usuario):

    sourceHtml = "<html><body><p>Hola " + usuario + " Diploma de particiacion</p></body></html>"

    outputFilename = settings.MEDIA_ROOT + '/pdf/diploma.pdf'
    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result

    resultFile.close()

    sourceHtml = "<html><body><p>" + usuario + "To PDF or not to PDF</p></body></html>"

    outputFilename = settings.MEDIA_ROOT + '/pdf/invitacion.pdf'
    resultFile = open(outputFilename, "w+b")

    pisaStatus = pisa.CreatePDF(
        sourceHtml,  # the HTML to convert
        dest=resultFile)  # file handle to recieve result

    resultFile.close()

    return outputFilename


def completarRegistro(request, next):
    perfil = request.user.profile
    if perfil.alimentary_restriction and perfil.entry_country and perfil.entry_port and perfil.entry_country_date and perfil.health_consideration and perfil.identification and perfil.letter and perfil.out_country and perfil.out_country_date and perfil.out_port:
        if next == '':
            return redirect('index')
        return redirect(next)
    else:
        messages.add_message(request, messages.WARNING, 'Por favor complete su registro')
        return redirect('edit_profile', perfil.pk)


def salir(request):
    return logout(request, next_page='index')