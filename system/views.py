from django.shortcuts import render
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required
from system.forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    template_response = views.login(request, authentication_form=Login_Form,
                                    template_name='users/identificarse.html')
    return template_response


@login_required()
def logout(request):
    template_response = views.logout(request, next_page='Index')
    return template_response
