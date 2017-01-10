# -*- coding: utf-8 -*-
from registration.forms import *
from system.models import *

#formulario de creacion de usuarios  quitar al final


class ProfileForm(RegistrationForm):
    name = forms.CharField(label='Name', required=True, )
    last_name = forms.CharField(label='Last name', required=True)
    gender = forms.ChoiceField(label='Gender', required=True, choices=[('m', 'Male'), ('f', 'Female'), ])
    born_date = forms.DateField(label='Born date', required=True, widget=forms.TextInput(attrs={'class':'datepicker'}))
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


class TshirtForm(forms.ModelForm):
    class Meta:
        model = Tshirt
        fields = ['size', 'amount']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'gender', 'born_date', 'nationality', 'institution', 'identification',
                  'alimentary_restriction', 'health_consideration', 'snore', 'letter', 'entry_country', 'out_country',
                  'entry_port', 'out_port', 'entry_country_date', 'out_country_date', ]
        widgets = {
            'entry_country_date': forms.TextInput(attrs={'class': 'datepicker'}),
            'out_country_date': forms.TextInput(attrs={'class': 'datepicker'}),
        }