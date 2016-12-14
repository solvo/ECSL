from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin



def forum(request):
    return render(request, 'foro/foro.html')


class mesas(ListView):
    template_name = 'actividades/mesas/list_mesas.html'
    queryset = Speech.objects.filter(speech_type=1)


class view_table(DetailView):
    template_name = 'actividades/mesas/view_table.html'
    model = Speech
