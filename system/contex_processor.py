# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse


def menu(request):
    menu = {'menu': [
                     {'name': 'Site', 'url': reverse('Index')}
                     ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu


def menu_user(request):
    menu = {'menu': [{'name': 'Register', 'url': reverse('registration_register')},
                     {'name': 'Login', 'url': reverse('auth_login')},
                     {'name': 'Site', 'url': reverse('Index')}
                     ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu
