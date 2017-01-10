# -*- coding: utf-8 -*-
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from system.forms import *
from django.http import Http404
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


@method_decorator(login_required, name='dispatch')
class foro(ListView):
    queryset = Topic.objects.all().order_by('-date_created')
    template_name = 'foro/foro.html'


@method_decorator(login_required, name='dispatch')
class foro_topic(ListView):

    template_name = 'foro/foro_topic.html'
    context_object_name = 'topic_list'

    def get_queryset(self, *args, **kwargs):
        self.editor = self.kwargs['slug']
        return Speech.objects.filter(topic__slug = self.editor).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super(foro_topic, self).get_context_data(**kwargs)
        context['topic'] = Topic.objects.get(slug=self.editor)

        return context


@method_decorator(login_required, name='dispatch')
class foro_detail(ListView):

    template_name = 'foro/foro_detail.html'
    context_object_name = 'speech_details'

    def get_queryset(self, *args, **kwargs):
        self.editor = self.kwargs['slug']
        self.detalles = self.kwargs['slug1']
        return Speech.objects.get(topic__slug= self.editor, slug=self.detalles)


@method_decorator(login_required, name='dispatch')
class foro_types(ListView):

    template_name = 'foro/foro_types.html'
    context_object_name = 'foro_types'

    def get_queryset(self, *args, **kwargs):
        self.types = self.kwargs['slug']
        return Speech.objects.filter(speech_type__slug= self.types)


@method_decorator(login_required, name='dispatch')
class insert_speech(SuccessMessageMixin, CreateView):
    template_name = 'foro/insert_speech.html'
    model = Speech
    form_class = InsertSpeech
    success_url = '/activity/'
    success_message = "La actividad fue creada. Necesita la aprobación de un administrador"

    def get(self, request, *arg, **kwargs):
        try:
            self.speech_slug = get_object_or_404(Speech, slug= self.kwargs['slug'])

        except Http404:

            self.topic_slug = get_object_or_404(Topic, slug= self.kwargs['slug'])

        return super(insert_speech, self).get(request, *arg, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.topic_slug = get_object_or_404(Topic, slug= self.kwargs['slug'])
        form.instance.topic = self.topic_slug
        form.instance.slug = slugify(form.instance.user.username + ' ' + form.instance.title)
        return super(insert_speech, self).form_valid(form)