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
    url(r'^accounts/completar_registro/(?P<next>[\S]*)$', completarRegistro, name='completar_registro'),
    url(r'^accounts/salir$', salir, name='salir'),

]

forum_patterns = [

    url(r'^activity/$', foro.as_view(), name='Forum'),
    url(r'^activity/(?P<slug>[\w-]+)/insert_speech/$', insert_speech.as_view(), name='Insert_Speech'),
    url(r'^activity/(?P<slug>[\w-]+)/$', foro_topic.as_view(), name='Forum_Topic'),
    url(r'^activity/(?P<slug>[\w-]+)/(?P<slug1>[\w-]+)/$', foro_detail.as_view(), name='Forum_Detail'),
    url(r'^activity/filter/type/(?P<slug>[\w-]+)/$', foro_types.as_view(), name='Forum_Types'),
    url(r'^activity/(?P<speech_id>[0-9]+)/nuevo_recurso$', subirRecurso.as_view(), name='subir_recurso'),

]

ajax_patterns = [

        # Esto es lo de los sistemas por ajax
    url(r'^ajax/enroll/', matricularse, name='ajax_matricula'),
    url(r'^ajax/delete_enroll/', deleteMatricularse, name='ajax_delete_matricula'),
    url(r'^ajax/add_like/$', profileAddLike, name='add_like'),
    url(r'^ajax/camisetas_pendientes/$', camisetas_pendientes, name='camisetas_pendientes'),
    url(r'^ajax/delete_pedido/$', deletePedido, name='ajax_delete_pedido'),
    url(r'^ajax/agregar_pedido/$', agregar_pedido, name='ajax_agregar_pedido'),
    url(r'^ajax/delete_recurso/', deleteRecurso, name='ajax_delete_recurso'),

]

tshirt_patterns = [
        # Esto es lo de las camisetas
    url(r'^carrito/pagar_pedido/(?P<pedido_id>[0-9]+)/$', pagarPedido, name='pagar_pedido'),
    url(r'^ajax/editar_pedido/$', editarPedido, name='editar_pedido'),
    url(r'^carrito/pagar_todos/$', pagarTodo, name='pagar_todo'),
    url(r'^carrito/$', Carrito.as_view(), name='carrito'),
    url(r'^tshirt/$', tshirt_list.as_view(), name='tshirt'),

]


urlpatterns = user_patterns + extra_patterns + forum_patterns + tshirt_patterns + ajax_patterns + [

    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^testing$', testing, name='Testing'), #esto es pa probar quitar al final

    url(r'^media/$', testing, name='Media'), #esto es pa probar quitar al final
    url(r'^calender/$', agenda, name='Agenda'),

    url(r'^faq/$', faq.as_view(), name='faq'),
    url(r'^becas/$', becas.as_view(), name='becas'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

