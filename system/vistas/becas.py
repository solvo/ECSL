from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin


@method_decorator(login_required, name='dispatch')
class becas(CreateView, SuccessMessageMixin):
    template_name = 'becas/becas.html'
    model = Inscription
    context_object_name = 'becas'
    success_url = '/'
    fields = ['mozilla_subvention_description']
    success_message = 'Tu propuesta ha sido enviada. Necesita la aprobacion de un administrador'

    def form_valid(self, form):
        form.instance.subvention_request = True
        form.instance.user = self.request.user
        form.instance.preregistered = True

        return super(becas, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not Inscription.objects.filter(user=self.request.user):
            return super(becas, self).dispatch(request, *args, **kwargs)

        estado = Inscription.objects.get(user=self.request.user)
        if estado.subvention_request and estado.not_registered and estado.registered:
            return render(self.request, 'becas/becas.html', {'estado': 'Analizando'})
        elif estado.subvention_request and estado.not_registered == False and estado.registered:
            return render(self.request, 'becas/becas.html', {'estado': 'Ha sido Aprobado'})

        elif estado.subvention_request and estado.not_registered and estado.registered ==False:
            return render(self.request, 'becas/becas.html', {'estado': 'Denegado'})
        elif estado.subvention_request and estado.not_registered == False and estado.registered == False:
            return render(self.request, 'becas/becas.html', {'estado': 'Analizando'})
