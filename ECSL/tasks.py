from __future__ import absolute_import
from ECSL.celery import app


@app.task
def addNum():
    print('sdfsdfsdf')
