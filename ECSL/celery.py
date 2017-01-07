# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings
# from celery import shared_task
#
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECSL.settings')
# app = Celery('ECSL')
#
#
# app.config_from_object('django.conf:settings')
#
#
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
#
#
# @shared_task
# def envios_correo():
#
#     print('sdfsdfsdf')
