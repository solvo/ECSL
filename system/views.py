# -*- coding: utf-8 -*-
from system.forms import *
from django.shortcuts import render
from django.views.generic import *


def index(request):

    return render(request, 'index.html', {'types': SpeechType.objects.all()})


class subirRecurso(CreateView):
    model = SpeechResource
    fields = ('recurso', 'speech', )
    template_name = 'foro/subir_recurso.html'
