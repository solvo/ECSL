from django.shortcuts import render, reverse, redirect
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from system.forms import *
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.views.generic.detail import SingleObjectMixin


@method_decorator(login_required, name='dispatch')
class profile(CreateView, SingleObjectMixin):
    template_name = 'usuarios/profile.html'
    model = Profile
    success_url = '/'
    fields = ['alimentary_restriction', 'born_date', 'gender', 'health_consideration',
              'identification', 'institution', 'nationality', 'snore']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(profile, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        ty = User.objects.get(pk=request.user.pk)
        try:
            ty.profile.DoesNotExist
        except ObjectDoesNotExist:

            return super(profile, self).dispatch(request, *args, **kwargs)
        else:

            return redirect('Index')


def testing(request):

    return render(request, 'testing.html')