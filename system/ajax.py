from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django_ajax.decorators import ajax
from django.contrib import messages


@login_required()
def notificaciones(request):
    return render(request, 'notificaciones.html')


@ajax
def matricularse(request, pk):
    print(pk)
    messages.add_message(request, messages.SUCCESS,
                         'Click in enoroll')
    return {
        'inner-fragments': {
            '.notificaciones': '<script>recargarMensajes();</script>'

        },
    }


@ajax
def matricularse_tables(request, pk):

    messages.add_message(request, messages.SUCCESS,'Click in enoroll')
    return {
            'inner-fragments': {
                '.notificaciones': '<script> recargarMensajes();</script>'}, }
