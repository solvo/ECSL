from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin


@method_decorator(login_required, name='dispatch')
class edit_profile(UpdateView):
    template_name = 'usuarios/edit_profile.html'
    model = Profile

    fields = ['alimentary_restriction', 'born_date', 'gender', 'health_consideration',
              'identification', 'institution', 'nationality', 'snore',
              'entry_country', 'out_country', 'entry_port', 'out_port',
              'entry_country_date', 'out_country_date', 'letter']


@method_decorator(login_required, name='dispatch')
class view_profile(DetailView):
    template_name = 'usuarios/view_profile.html'
    model = Profile


@login_required()
def testing(request):
 all_s = Speech.objects.filter(user__profile__in=Profile.objects.all())
    for aa in all_s:

        send_mail('Comienzo del curso', 'Hola ' + aa.user.username + ' usted se registro en el curso: '
                  + aa.title + ' el cual comenzara en unos 10 minutos y tendra lugar en: : ' + aa.places
                  + ' por favor no falte atentamente el Administrador', 'chicomtz.sr@gmail.com',
                  [aa.user.email, ])


    return render(request, 'testing.html')