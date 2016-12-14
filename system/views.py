# -*- coding: utf-8 -*-
from django.shortcuts import render
from system.models import *
from system.forms import *
from django.contrib import messages
from django.shortcuts import render, redirect
from registration.backends.hmac.views import RegistrationView
from registration import signals


def index(request):
    pre_matricula = False

    try:
        pp = User.objects.get(pk=request.user.pk)
        profile_pk = pp.profile.pk

    except ObjectDoesNotExist:
        user_without_profile={'status': pre_matricula, 'user_pk': request.user.pk}
        return render(request, 'index.html', user_without_profile)

    periodo = get_active_period()

    if periodo == 0:
        pre_matricula = True
        user_with_profile = {'status': pre_matricula, 'profile_pk': profile_pk, 'user_pk': request.user.pk}
        return render(request, 'index.html', user_with_profile)
    without_user = {'status': pre_matricula}
    return render(request, 'index.html', without_user)


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
