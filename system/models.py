from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _

# Faltan Question y Question Category


class Profile(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    alimentary_restriction = TextField(verbose_name=_('Food Restriction'))
    born_date = DateField(verbose_name=_('Born Date'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Gender'))
    health_consideration = TextField(verbose_name=_('Health Considerations'))
    identification = CharField(max_length=12, verbose_name=_('Identification'))
    institution = CharField(max_length=12, verbose_name=_('Institution'))
    nationality = CharField(max_length=12, verbose_name=_('Nationality'))
    snore = BooleanField(verbose_name=_('Snore?'))


class Inscription(Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    mozilla_subvention = BooleanField(verbose_name=_('Mozilla Subvention?'))
    mozilla_subvention_description = TextField(verbose_name=_('Mozilla Subvention Description'))
    payed = BooleanField(verbose_name=_('Payed?'))
    preregistered = BooleanField(verbose_name=_('Preregistered'))
    registered = BooleanField(verbose_name=_('Registered'))
    subvention_description = TextField(verbose_name=_('Subvention Description'))  # Preguntar para que es
    subvention_request = BooleanField(verbose_name=_('Subvention Request'))


class TshirtStyle(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    description = TextField(verbose_name=_('Description'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Gender'))
    img1 = ImageField(verbose_name=_('Image 1'))
    img2 = ImageField(verbose_name=_('Image 2'))
    img3 = ImageField(verbose_name=_('Image 3'))
    name = CharField(max_length=45, verbose_name=_('Name'))
    price = DecimalField(verbose_name=_('Image 1'), decimal_places=2, max_digits=6)


class Tshirt(Model):
    style = ForeignKey(TshirtStyle, on_delete=CASCADE, verbose_name=_('Style'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('User'))
    amount = PositiveIntegerField(verbose_name=_('Amount'))
    last_update = DateField(verbose_name=_('Last Update'))
    size = CharField(max_length=15, verbose_name=_('Size'))


class SpeechType(Model):
    name = CharField(max_length=45,verbose_name=_('Name'))


class Topic(Model):
    name = CharField(max_length=45, verbose_name=_('Name'))


class Speech (Model):
    speech_type = ForeignKey(SpeechType, verbose_name=_('Speech Type'))
    topic = ForeignKey(Topic, verbose_name=_('Topic'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('User'))
    audience = TextField(verbose_name=_('Audience')) # Aclarar para que se usa este campo
    description = TextField(verbose_name=_('Description'))
    notes = TextField(verbose_name=_('Notes'))
    skill_level = PositiveIntegerField(verbose_name=_('Skill Level'))
    speaker_information = TextField(verbose_name=_('Speaker Information'))
    title = TextField(verbose_name=_('Title'))