from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ECSL.settings')
app = Celery('ECSL')


app.config_from_object('django.conf:settings')


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def add(x, y):
    return x * y


@app.task(name='task.resta_task')
def resta(x, y):
    return x - y
