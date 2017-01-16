from PIL.ImageChops import add_modulo
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponseBadRequest
from system.forms import TshirtForm
from django.utils.timezone import now

@method_decorator(login_required, name='dispatch')
class tshirt_list(ListView):
    template_name = 'Tshirt/Tshirt.html'
    model = TshirtStyle
    context_object_name = 'camisetas'

    def get_context_data(self, **kwargs):
        context = super(tshirt_list, self).get_context_data(**kwargs)
        context['form'] = TshirtForm
        return context


class Carrito(ListView, LoginRequiredMixin):
    template_name = 'Tshirt/carrito.html'
    queryset = Tshirt.objects.filter(pagada=False)
    context_object_name = 'camisetas'


# pagar un solo pedido
@login_required()
def pagarPedido(request, pedido_id):
    tshirt = Tshirt.objects.get(pk=pedido_id)
    # Aqui debe ir la funcion qu permite pagar por PayPal
    tshirt.pagada = True
    tshirt.save()
    messages.add_message(request, messages.SUCCESS, 'Gracias por comprar las camisetas del evento')
    return redirect('carrito')


@login_required()
def editarPedido(request):

    id_pedido = request.POST['id_pedido']
    elemento = Tshirt.objects.get(pk=id_pedido)
    amount = request.POST['amount']
    gender_data = request.POST['id_gender']
    elemento.amount = amount
    elemento.gender = gender_data
    elemento.save()
    return JsonResponse({'mensaje': "Pedido eliminado"})


# pagar todos los pedidos del usuario autenticado
@login_required()
def pagarTodo(request):
    camisetas = Tshirt.objects.filter(user=request.user)
    # Aqui debe ir la funcion qu permite pagar por PayPal
    for tshirt in camisetas:
        tshirt.pagada = True
        tshirt.save()
    messages.add_message(request, messages.SUCCESS, 'Gracias por comprar las camisetas del evento')
    return redirect('tshirt')


@login_required()
def deletePedido(request):
    user = request.user
    id_pedido = request.POST['id_pedido']
    print id_pedido
    camiseta = get_object_or_404(Tshirt, pk=id_pedido)
    if user != camiseta.user:
        return HttpResponseBadRequest()
    else:
        camiseta.delete()
    return JsonResponse({'mensaje': "Pedido eliminado"})


@login_required()
def agregar_pedido(request):
    user = request.user
    amount = request.POST['amount']
    talla = request.POST['talla']
    gender = request.POST['id_gender']
    id_sty = request.POST['id_style']

    obj = TshirtStyle.objects.get(pk=id_sty)
    Tshirt.objects.create(user=user, style=obj, amount=amount, last_update=now(), size=talla, gender=gender)
    return JsonResponse({'id_camiseta': Tshirt.objects.last().pk})


# para poder saber las camisetas sin pagar mediante ajax pa los fronten cuando eliminen un pedido
# por ajax actualicen el indice de camisetas pendientes en el base
@login_required()
def camisetas_pendientes(request):
    user = request.user
    pendientes = user.profile.camisetas_sin_pagar
    return JsonResponse({'camisetas_pendientes': pendientes})
