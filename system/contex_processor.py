# -*- coding: UTF-8 -*-

from system.models import Profile, User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist


def menu(request):
    profile_pk = []
    try:
        pp = User.objects.get(pk=request.user.pk)
        profile_pk = pp.profile.pk
    except ObjectDoesNotExist:
        redirect('index')
    value = {'profile_pk': profile_pk}
    return value


def url(request):

    value = {'url':request.path}
    return value