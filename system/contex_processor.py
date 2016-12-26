# -*- coding: UTF-8 -*-
from system.models import Patrocinadores


def url(request):

    value = {'url': request.path}
    return value


def patrocinadores(request):

    value = {'imagen': Patrocinadores.objects.all()}
    return value

