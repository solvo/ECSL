# -*- coding: utf-8 -*-
from registration.forms import *
from functools import partial
from system.models import *

DateInput = partial(forms.DateInput, {'class': 'datepicker'})


#formulario de creacion de usuarios  quitar al final
class ProfileForm(RegistrationForm):
    name = forms.CharField(label='Name', required=True, )
    last_name = forms.CharField(label='Last name', required=True)
    gender = forms.ChoiceField(label='Gender', required=True, choices=[('m', 'Male'), ('f', 'Female'), ])
    born_date = forms.DateField(label='Born date', required=True, widget=DateInput())
    nationality = forms.CharField(label='Nationality', max_length=12, required=True)
    institution = forms.CharField(label='Institution', max_length=12, required=True)


class InsertTopic(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['name', 'description']


class InsertSpeech(forms.ModelForm):

    class Meta:
        model = Speech
        fields = ['title', 'description', 'notes', 'speaker_information','audience', 'skill_level',
                  'speech_type', 'topic']
