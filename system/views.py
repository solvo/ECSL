from django.shortcuts import render
from system.models import *



def index(request):
    pre_matricula = False
    total_speech = Speech.objects.all()
    try:
        pp = User.objects.get(pk=request.user.pk)
        profile_pk = pp.profile.pk

    except ObjectDoesNotExist:
        user_without_profile={'status': pre_matricula, 'total_speech': total_speech, 'user_pk': request.user.pk}
        return render(request, 'index.html', user_without_profile )

    periodo = get_active_period()

    if periodo == 0:
        pre_matricula = True
        user_with_profile = {'status': pre_matricula, 'profile_pk': profile_pk, 'user_pk': request.user.pk, 'total_speech': total_speech}
        return render(request, 'index.html', user_with_profile)
    without_user = {'status': pre_matricula, 'total_speech': total_speech}
    return render(request, 'index.html', without_user)
