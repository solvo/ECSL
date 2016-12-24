from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404


@method_decorator(login_required, name='dispatch')
class becas(CreateView, SuccessMessageMixin):
    template_name = 'becas/becas.html'
    model = Inscription
    context_object_name = 'becas'
    success_url = '/'
    fields = ['subvention_description']
    success_message = 'Tu propuesta ha sido enviada. Necesita la aprobacion de un administrador'

    def form_valid(self, form):

        form.instance.user = self.request.user
        if self.request.user.profile.enrolled:
            form.instance.preregistered = False
            form.instance.registered = True
        else:
            form.instance.preregistered = True
            form.instance.registered = False
        return super(becas, self).form_valid(form)
