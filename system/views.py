# -*- coding: utf-8 -*-
from system.forms import *
from django.views.generic import *
from django.shortcuts import render, get_object_or_404


def index(request):

    return render(request, 'index.html', {'types': SpeechType.objects.all()})


class subirRecurso(CreateView):
    model = SpeechResource
    fields = ('recurso', )
    template_name = 'foro/subir_recurso.html'

    def form_valid(self, form):
        form.instance.speech = get_object_or_404(Speech, pk= self.kwargs['speech_id'])
        return super(subirRecurso, self).form_valid(form)