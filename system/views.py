# -*- coding: utf-8 -*-
from django.shortcuts import render
from system.models import *
from system.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from registration.views import RegistrationView


def index(request):
    pre_matricula = False
    total_speech = Speech.objects.all()
    try:
        pp = User.objects.get(pk=request.user.pk)
        profile_pk = pp.profile.pk

    except ObjectDoesNotExist:
        user_without_profile={'status': pre_matricula, 'total_speech': total_speech, 'user_pk': request.user.pk}
        return render(request, 'index.html', user_without_profile)

    periodo = get_active_period()

    if periodo == 0:
        pre_matricula = True
        user_with_profile = {'status': pre_matricula, 'profile_pk': profile_pk, 'user_pk': request.user.pk, 'total_speech': total_speech}
        return render(request, 'index.html', user_with_profile)
    without_user = {'status': pre_matricula, 'total_speech': total_speech}
    return render(request, 'index.html', without_user)


def create_profile(request):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            formuser = RegistrationForm(data={'username': form.cleaned_data["username"], 'email': form.cleaned_data["email"], 'password1': form.cleaned_data["password1"],
                                              'password2': form.cleaned_data["password2"]})
            if formuser.is_valid():
                user = formuser.save()
                profile = Profile(name=form.cleaned_data["name"], last_name=form.cleaned_data["last_name"],
                                  gender=form.cleaned_data["gender"], user=user,
                                  born_date=form.cleaned_data["born_date"],
                                  nationality=form.cleaned_data["nationality"],
                                  institution=form.cleaned_data["institution"],)
                profile.save()
                messages.add_message(request, messages.SUCCESS, 'The user '+ profile.user.username +'was created susesfully ')
                return redirect('index')
    return render(request, 'usuarios/create_profile.html', {'form': form})