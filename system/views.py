# -*- coding: utf-8 -*-
from django.shortcuts import render
from system.models import *
from system.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from registration.backends.hmac.views import RegistrationView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from registration import signals
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from xhtml2pdf import pisa  # import python module


def index(request):

    return render(request, 'index.html', {'types': SpeechType.objects.all()})


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


        # Define your data
        sourceHtml = "<html><body><p>To PDF or not to PDF</p></body></html>"
        outputFilename = "test.pdf"

        # Utility function


        # open output file for writing (truncated binary)
        resultFile = open(outputFilename, "w+b")
        # convert HTML to PDF
        pisaStatus = pisa.CreatePDF(
            sourceHtml,  # the HTML to convert
            dest=resultFile)  # file handle to recieve result
        # close output file
          # close output file
        # return True on success and False on errors


        resultFile.close()

        profile.save()
        return new_user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', 'last_name', 'gender', 'born_date', 'nationality', 'institution', 'identification',
              'alimentary_restriction', 'health_consideration', 'snore', 'letter', 'entry_country', 'out_country',
              'entry_port', 'out_port', 'entry_country_date', 'out_country_date', ]

    template_name = 'usuarios/my_edit_profile.html'
    success_url = "/"
    model = Profile


# esto es lo de dar like
@login_required()
def profileAddLike(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.likes.add(speech)
    return JsonResponse({'messages': "Me gusta confirmado"})


@login_required()
def matricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.add(speech)
    return JsonResponse({'messages': "Matricula confirmada"})


@login_required()
def deleteMatricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.remove(speech)
    return JsonResponse({'mensaje': "Matricula eliminada"})




