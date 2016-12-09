from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from system.forms import *
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator


def login(request):
    template_response = views.login(request, authentication_form=Login_Form,
                                    template_name='usuarios/identificarse.html')
    return template_response


@method_decorator(login_required, name='dispatch')
class profile(CreateView):
    template_name = 'usuarios/profile.html'
    model = Profile
    success_url = '/'
    fields = ['alimentary_restriction', 'born_date', 'gender', 'health_consideration',
              'identification', 'institution', 'nationality', 'snore']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(profile, self).form_valid(form)