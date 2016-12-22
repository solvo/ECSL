"""ECSL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from system.views import *
from system.vistas.User import *

from system.vistas.Agenda import *

from system.vistas.Speech import *
from system.ajax import *

extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    ]
urlpatterns = extra_patterns + [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^testing$', testing, name='Testing'), #esto es pa probar quitar al final


    url(r'^accounts/view_profile/(?P<pk>[\w-]+)/$', view_profile.as_view(), name='View_Profile'),
    url(r'^accounts/new_profile/$', createProfile.as_view(), name='New_Profile'),

    url(r'^accounts/edit_profile/(?P<pk>[0-9]+)$', ProfileUpdateView.as_view(), name='edit_profile'),



    url(r'^forum/$', foro.as_view(), name='Forum'),
    url(r'^forum/insert_topic/$', insert_topic.as_view(), name='Insert_Topic'),
    url(r'^forum/(?P<slug>[\w-]+)/insert_speech/$', insert_speech.as_view(), name='Insert_Speech'),


    url(r'^agenda/$', agenda.as_view(), name='Agenda'),

    url(r'^forum/(?P<slug>[\w-]+)/$', foro_topic.as_view(), name='Forum_Topic'),
    url(r'^forum/(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$', foro_detail.as_view(), name='Forum_Detail'),


]

