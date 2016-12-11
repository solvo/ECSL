from django.shortcuts import render
from system.models import *


def index(request):
    pre_matricula = False
    pp = User.objects.get(pk=request.user.pk)
    profile_pk=pp.profile.pk

    periodo = get_active_period()
    if periodo == 0:
        pre_matricula = True
        return render(request, 'index.html', {'status': pre_matricula, 'profile_pk': profile_pk})
    return render(request, 'index.html', {'status': pre_matricula})
