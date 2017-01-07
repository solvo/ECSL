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
from system.vistas.FAQ import *
from system.vistas.Agenda import *
from system.vistas.Speech import *
from system.vistas.Tshirt import *
from system.vistas.becas import *
from system.ajax import *
from django.conf.urls.static import static
from django.conf import settings

extra_patterns = [

    url(r'^accounts/', include('registration.backends.hmac.urls')),

    ]

user_patterns = [

    url(r'^accounts/view_profile/(?P<pk>[\w-]+)/$', view_profile.as_view(), name='View_Profile'),
    url(r'^accounts/new_profile/$', createProfile.as_view(), name='New_Profile'),
    url(r'^accounts/edit_profile/(?P<pk>[0-9]+)$', ProfileUpdateView.as_view(), name='edit_profile'),

]

forum_patterns = [

    url(r'^activity/$', foro.as_view(), name='Forum'),
    url(r'^activity/(?P<slug>[\w-]+)/insert_speech/$', insert_speech.as_view(), name='Insert_Speech'),
    url(r'^activity/(?P<slug>[\w-]+)/$', foro_topic.as_view(), name='Forum_Topic'),
    url(r'^activity/(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$', foro_detail.as_view(), name='Forum_Detail'),
    url(r'^activity/filter/type/(?P<slug>[\w-]+)/$', foro_types.as_view(), name='Forum_Types'),
]

ajax_patterns = [
        # Esto es lo de matricularse ------------
    url(r'^ajax/enroll/', matricularse, name='ajax_matricula'),
    url(r'^ajax/delete_enroll/', deleteMatricularse, name='ajax_delete_matricula'),
    # Esto es lo de dar like -------------------------
    url(r'^ajax/add_like/$', profileAddLike, name='add_like'),
]


urlpatterns = user_patterns + extra_patterns + forum_patterns + ajax_patterns + [

    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^testing$', testing, name='Testing'), #esto es pa probar quitar al final

    url(r'^media/$', testing, name='Media'), #esto es pa probar quitar al final


    url(r'^calender/$', agenda.as_view(), name='Agenda'),

    url(r'^tshirt/$', tshirt_list.as_view(), name='tshirt'),
    url(r'^faq/$', faq.as_view(), name='faq'),
    url(r'^becas/$', becas.as_view(), name='becas'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

