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


def index(request):

    return render(request, 'index.html')


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
    return JsonResponse({'mensaje': "Me gusta confirmado"})


@login_required()
def matricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.add(speech)
    return JsonResponse({'mensaje': "Matricula confirmada"})


@login_required()
def deleteMatricularse(request):
    profile = request.user.profile
    idSpeech = request.POST['id_speech']
    speech = get_object_or_404(Speech, pk=idSpeech)
    profile.matriculatedspeechs.remove(speech)
    return JsonResponse({'mensaje': "Matricula eliminada"})




