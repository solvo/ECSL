from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin


class mesas(ListView):
    template_name = 'actividades/mesas/list_mesas.html'
    queryset = Speech.objects.filter(speech_type=1)