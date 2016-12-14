# -*- coding: utf-8 -*-
from django.forms import ModelForm
from system.models import Profile
from registration.forms import *


#formulario de creacion de usuarios  quitar al final
class ProfileForm(RegistrationForm):
    name = forms.CharField(label='Name', required=True, )
    last_name = forms.CharField(label='Last name', required=True)
    gender = forms.ChoiceField(label='Gender', required=True, choices=[('m', 'Male'), ('f', 'Female'), ])
    born_date = forms.DateField(label='Born date', required=True)
    nationality = forms.CharField(label='Nationality', max_length=12, required=True)
    institution = forms.CharField(label='Institution', max_length=12, required=True)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)



