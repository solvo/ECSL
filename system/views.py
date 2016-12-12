from django.shortcuts import render
from system.models import *


def index(request):
    pre_matricula = False
    total_speech = Speech.objects.all()
    try:
        pp = User.objects.get(pk=request.user.pk)
        profile_pk = pp.profile.pk

    except ObjectDoesNotExist:
        return render(request, 'index.html', {'status': pre_matricula, 'total_speech': total_speech})

    periodo = get_active_period()

    if periodo == 0:
        pre_matricula = True
        return render(request, 'index.html', {'status': pre_matricula, 'profile_pk': profile_pk, 'user_pk': request.user.pk, 'total_speech': total_speech})
    return render(request, 'index.html', {'status': pre_matricula, 'total_speech': total_speech})
