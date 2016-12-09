# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm, SetPasswordForm, UserCreationForm


class Login_Form(AuthenticationForm, SetPasswordForm):
    pass


class ChancePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña actual:', max_length=150,
                                   widget=forms.PasswordInput())
    new_password1 = forms.CharField(label='Nueva Contraseña:', max_length=150,
                                    widget=forms.PasswordInput())
    new_password2 = forms.CharField(label='Repetir Contraseña:', max_length=150,
                                    widget=forms.PasswordInput())
