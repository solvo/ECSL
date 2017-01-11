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

    dia20 = Speech.objects.filter(published=True).filter(pepe__day=20)
    dia21 = Speech.objects.filter(published=True).filter(pepe__day=21)
    lista = []
    if dia20.count() < dia21.count():
        mayor = dia21.count()
    else:
        mayor = dia20.count()
    for ii in range(0, mayor):

        var20 = ''
        var21 = ''

        if ii < dia20.count():
            var20 = dia20[ii]

        if ii < dia21.count():
            var21 = dia21[ii]

        dicc = {'dia20': var20, 'dia21': var21}
        lista.append(dicc)

    print(lista)

    return render(request, 'agenda/agenda.html', {'lista': lista})
