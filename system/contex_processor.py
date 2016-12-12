# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse


def menu(request):
    menu = {'menu': [
                     {'name': 'Site', 'url': reverse('Index')},
                     {'name': 'Testing', 'url':reverse('Testing')},
                     {'name': 'Register', 'url':reverse('registration_register')},
                     {'name': 'Logout', 'url':reverse('auth_logout')},
                     {'name': 'Login', 'url':reverse('auth_login')},
                     ]}

    for item in menu['menu']:
        if request.path == item['url']:
            item['active'] = True
    return menu