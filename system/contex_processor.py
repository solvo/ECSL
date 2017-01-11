# -*- coding: UTF-8 -*-
from system.models import *


def url(request):

    value = {'url': request.path}
    return value


def patrocinadores(request):

    value = {'imagen': Patrocinadores.objects.all()}
    return value


def camisetas(request):
    user = request.user
    if not user.is_anonymous:
        value = {'pedidos': Tshirt.objects.filter(user=user)}
        return value
    else:
        value = ''
        return value


