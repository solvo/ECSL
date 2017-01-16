from django.shortcuts import render
from system.forms import *


def agenda(request):

    dia20 = Speech.objects.filter(published=True).filter(activity_start__day=20)
    dia21 = Speech.objects.filter(published=True).filter(activity_start__day=21)
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
