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
from system.vistas.Speech import *
from system.ajax import *

extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    ]
urlpatterns = extra_patterns + [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^testing$', testing, name='Testing'), #esto es pa probar quitar al final
    url(r'^accounts/profile/$', profile.as_view(), name='Profile'),
    url(r'^accounts/edit_profile/(?P<pk>[\w-]+)/$', edit_profile.as_view(), name='Edit_Profile'),
    url(r'^accounts/view_profile/(?P<pk>[\w-]+)/$', view_profile.as_view(), name='View_Profile'),
    url(r'^accounts/edit_account/(?P<pk>[\w-]+)/$', edit_account.as_view(), name='Edit_Account'),

    url(r'^accounts/new_profile/$', createProfile.as_view(), name='New_Profile'),



    url(r'^forum/$', forum, name='Forum'),
    url(r'^forum/tables/$', tables.as_view(), name='Tables'),
    url(r'^forum/tables/view_tables/(?P<pk>[\w-]+)/$', view_table.as_view(), name='View_Table'),

    url(r'^forum/dialog/$', dialog.as_view(), name='Dialog'),
    url(r'^forum/dialog/view_dialog/(?P<pk>[\w-]+)/$', view_dialog.as_view(), name='View_Dialog'),

    url(r'^forum/talleres/$', talleres.as_view(), name='Talleres'),
    url(r'^forum/talleres/view_talleres/(?P<pk>[\w-]+)/$', view_talleres.as_view(), name='View_Talleres'),

    url(r'^ajax/matricularse/(?P<pk>[\w-]+)/$', matricularse, name='Ajax_Talleres'),
    url(r'^notificaciones/$', notificaciones, name='notificaciones'),




]

