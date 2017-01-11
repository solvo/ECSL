from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from system.forms import *
from django.http import Http404


def agenda(request):
    day20 = Speech.objects.filter(published=True).filter(pepe__day=20).order_by('-pepe')
    day21 = Speech.objects.filter(published=True).filter(pepe__day=21).order_by('-pepe')
    dicc = {}

    if day20.count() < day21.count():
        mayor = day21.count()
    else:
        mayor = day20.count()

    for ii in range(0, mayor):

        if ii < day20.count():
            dicc = {'v20': day20[ii].title, }

        else:
            dicc = {'v20': '', }
        if ii < day21.count():
            dicc = {'v21': day21[ii].title, }

        else:
            dicc = {'v21': '', }

    return render(request, 'agenda/agenda.html')
