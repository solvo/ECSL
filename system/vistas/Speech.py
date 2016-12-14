from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator


@login_required()
def forum(request):

    return render(request, 'foro/foro.html', {'user_pk': request.user.pk})


@method_decorator(login_required, name='dispatch')
class tables(ListView):
    template_name = 'actividades/mesas/list_table.html'
    queryset = Speech.objects.filter(speech_type=1)

    def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
        context = super(tables, self).get_context_data(**kwargs)
    # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context


@method_decorator(login_required, name='dispatch')
class view_table(DetailView):
    template_name = 'actividades/mesas/view_table.html'
    model = Speech

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(view_table, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context


@method_decorator(login_required, name='dispatch')
class dialog(ListView):
    template_name = 'actividades/dialogos/list_dialog.html'
    queryset = Speech.objects.filter(speech_type=3)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(dialog, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context


@method_decorator(login_required, name='dispatch')
class view_dialog(DetailView):
    template_name = 'actividades/dialogos/view_dialog.html'
    model = Speech

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(view_dialog, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context


@method_decorator(login_required, name='dispatch')
class talleres(ListView):
    template_name = 'actividades/talleres/list_talleres.html'
    queryset = Speech.objects.filter(speech_type=2)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(talleres, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context


@method_decorator(login_required, name='dispatch')
class view_talleres(DetailView):
    template_name = 'actividades/talleres/view_talleres.html'
    model = Speech

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(view_talleres, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['user_pk'] = self.request.user.pk
        return context
