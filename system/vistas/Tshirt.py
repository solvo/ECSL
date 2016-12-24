from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class tshirt_list(ListView):
    template_name = 'Tshirt/Tshirt.html'
    model = Tshirt
    context_object_name = 'camisetas'
