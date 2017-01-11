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
    value = {'pedidos': Tshirt.objects.filter(user=user)}
    return value

