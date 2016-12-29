from __future__ import absolute_import
from ECSL.celery import app
from celery import shared_task


@shared_task
def addRes():
    print('sdfsdfsdf')
