from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin


@method_decorator(login_required, name='dispatch')
class profile(CreateView, SingleObjectMixin):
    template_name = 'usuarios/create_profile.html'
    model = Profile
    success_url = '/'
    fields = ['alimentary_restriction', 'born_date', 'gender', 'health_consideration',
              'identification', 'institution', 'nationality', 'snore',
              'entry_country', 'out_country', 'entry_port', 'out_port',
              'entry_country_date', 'out_country_date', 'letter']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(profile, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):

        try:
            Profile.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return super(profile, self).dispatch(request, *args, **kwargs)

        else:
            return redirect('index')


@method_decorator(login_required, name='dispatch')
class edit_profile(UpdateView, SingleObjectMixin):
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

    return render(request, 'testing.html')