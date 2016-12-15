from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator


@login_required()
def forum(request):

    return render(request, 'foro/foro.html', {'user_pk': request.user.pk})


@method_decorator(login_required, name='dispatch')
class tables(ListView):
    template_name = 'actividades/mesas/list_table.html'
    queryset = Speech.objects.filter(speech_type=1)


@method_decorator(login_required, name='dispatch')
class view_table(DetailView):
    template_name = 'actividades/mesas/view_table.html'
    model = Speech


@method_decorator(login_required, name='dispatch')
class dialog(ListView):
    template_name = 'actividades/dialogos/list_dialog.html'
    queryset = Speech.objects.filter(speech_type=3)


@method_decorator(login_required, name='dispatch')
class view_dialog(DetailView):
    template_name = 'actividades/dialogos/view_dialog.html'
    model = Speech


@method_decorator(login_required, name='dispatch')
class talleres(ListView):
    template_name = 'actividades/talleres/list_talleres.html'
    queryset = Speech.objects.filter(speech_type=2)


@method_decorator(login_required, name='dispatch')
class topic_talleres(SingleObjectMixin, ListView):
    template_name = 'actividades/talleres/list_talleres.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(topic_talleres, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(topic_talleres, self).get_context_data(**kwargs)
        context['topic'] = self.object
        return context

    def get_queryset(self):
        return Speech.objects.filter(speech_type=2)


@method_decorator(login_required, name='dispatch')
class view_talleres(DetailView):
    template_name = 'actividades/talleres/view_talleres.html'
    model = Speech


class add_talleres(CreateView):
    template_name = 'usuarios/create_profile.html'
    model = Speech
    success_url = '/forum/talleres/'
    fields = ['speech_type','topic', 'audience', 'description', 'notes', 'skill_level', 'speaker_information', 'title']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.speech_type = 2
        return super(add_talleres, self).form_valid(form)