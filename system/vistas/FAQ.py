from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import *
from system.models import *
from django.utils.decorators import method_decorator


class faq(ListView):
    template_name = 'faq/faq.html'
    queryset = Question.objects.filter(published=True).order_by('-created')
    context_object_name = 'faq_list'
	