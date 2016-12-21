from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from django.views.generic.detail import SingleObjectMixin
from system.models import *
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from system.forms import *
from django.http import Http404


class agenda(ListView):
    template_name = 'agenda/agenda.html'
    queryset = Speech.objects.filter(published=True).order_by('-date_start')