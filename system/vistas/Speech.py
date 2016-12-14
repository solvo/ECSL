from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin


def forum(request):
    type_speech = SpeechType.objects.all()

    return render(request, 'foro/foro.html', {'type_speech': type_speech})


class tables(ListView):
    template_name = 'actividades/mesas/list_table.html'
    queryset = Speech.objects.filter(speech_type=1)


class view_table(DetailView):
    template_name = 'actividades/mesas/view_table.html'
    model = Speech


class dialog(ListView):
    template_name = 'actividades/dialogos/list_dialog.html'
    queryset = Speech.objects.filter(speech_type=1)


class view_dialog(DetailView):
    template_name = 'actividades/dialogos/view_dialog.html'
    model = Speech


class talleres(ListView):
    template_name = 'actividades/talleres/list_talleres.html'
    queryset = Speech.objects.filter(speech_type=1)


class view_talleres(DetailView):
    template_name = 'actividades/talleres/view_talleres.html'
    model = Speech
