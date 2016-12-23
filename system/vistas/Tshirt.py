from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify

from django.http import Http404


class tshirt_list(ListView):
    template_name = 'Tshirt/Tshirt.html'
    model = Tshirt
    context_object_name = 'camisetas'
