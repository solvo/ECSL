from django.shortcuts import render, reverse, redirect, get_object_or_404
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
def matricularse(request, slug_speech, slug_topic):
    tema = get_object_or_404(Topic, slug=slug_topic)
    activity = get_object_or_404(Speech, slug=slug_speech, topic__slug=slug_topic)

    messages.add_message(request, messages.SUCCESS,
                         'Click in enoroll')
    return {
        'inner-fragments': {
            '.notificaciones': '<script> alert("df"); </script>'

        },
   }