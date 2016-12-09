from django.shortcuts import render
from system.models import *


def index(request):
    pre_matricula = False
    periodo = get_active_period()
    if periodo == 0:
        pre_matricula = True
        return render(request, 'index.html', {'status': pre_matricula})
    return render(request, 'index.html',{'status': pre_matricula})
