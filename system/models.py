# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings


def get_active_period():
    period = DateState.objects.filter(start_date__lte=now(),
                                   finish_date__gte=now())
    if period.exists():
        return period.last()
    return 0


class Inscription(Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    mozilla_subvention = BooleanField(verbose_name=_('Mozilla Subvention?'), default=False)
    mozilla_subvention_description = TextField(verbose_name=_('Mozilla Subvention Description'))
    payed = BooleanField(verbose_name=_('Payed?'), default=False)
    preregistered = BooleanField(verbose_name=_('Preregistered'))
    registered = BooleanField(verbose_name=_('Registered'))
    subvention_description = TextField(verbose_name=_('Subvention Description'))  # Preguntar para que es
    subvention_request = BooleanField(verbose_name=_('Subvention Request'), default=False)

    def __str__(self):
        return self.user.username


class TshirtStyle(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    description = TextField(verbose_name=_('Description'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Gender'))
    #img1 = ImageField(verbose_name=_('Image 1'), upload_to='Tshirt/')
    #img2 = ImageField(verbose_name=_('Image 2'), upload_to='Tshirt/')
    #img3 = ImageField(verbose_name=_('Image 3'), upload_to='Tshirt/')

    name = CharField(max_length=45, verbose_name=_('Name'))
    price = DecimalField(verbose_name=_('Price'), decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Tshirt(Model):
    style = ForeignKey(TshirtStyle, on_delete=CASCADE, verbose_name=_('Style'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('User'))
    amount = PositiveIntegerField(verbose_name=_('Amount'))
    last_update = DateField(verbose_name=_('Last Update'))
    size = CharField(max_length=15, verbose_name=_('Size'))

    def __str__(self):
        return self.style.name + ' ' + self.style.description


class SpeechType(Model):
    speech_choice = (
        ('Talleres', 'Talleres'),
        ('Charlas', 'Charlas'),
        ('Dialogos', 'Dialogos')
    )

    speech_icons = (
        (settings.STATIC_URL + 'img/talleres.png', 'T'),
        (settings.STATIC_URL + 'img/charlas.png', 'CH'),
        (settings.STATIC_URL + 'img/dialogos.png', 'D')
    )
    name = CharField(max_length=45, verbose_name=_('Name'), choices=speech_choice)
    icons = CharField(max_length=45, verbose_name=_('Icons'), choices=speech_icons)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')

    def __str__(self):
        return self.name


class Topic(Model):

    name = CharField(max_length=45, verbose_name=_('Name'),unique=True)
    description = TextField(verbose_name=_('Description'))
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')
    date_created = DateTimeField(verbose_name=_('Created Date'), auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.slug


class Speech(Model):

    class Meta:
        ordering = ["date_created"]

    speech_audience = (
        ('PG', 'Publico General'),
        ('NB', 'Nivel Basico'),
        ('NI', 'Nivel Intermedio'),
        ('NA', 'Nivel Avanzado'),
        ('PRO', 'Profesional'),
    )

    speech_type = ForeignKey(SpeechType, verbose_name=_('Speech Type'))
    topic = ForeignKey(Topic, verbose_name=_('Topic'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('User'))
    audience = CharField(verbose_name=_('Audience'), choices=speech_audience, max_length=45)
    description = TextField(verbose_name=_('Description'))
    notes = TextField(verbose_name=_('Notes'))
    skill_level = PositiveIntegerField(verbose_name=_('Skill Level'))
    speaker_information = TextField(verbose_name=_('Speaker Information'))
    title = CharField(max_length=250, verbose_name=_('Title'))
    places = CharField(max_length=250, verbose_name=_('Places'), null=True)
    days = DateTimeField(verbose_name=_('Event Start'), null=True)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')
    date_start = DateTimeField(verbose_name=_('Start Date'), null=True)
    date_created = DateTimeField(verbose_name=_('Created Date'), auto_now_add=True)
    published = BooleanField(verbose_name=_('Published'), default=False)

    def __str__(self):
        return self.speech_type.name + ' de ' + self.topic.name


class Hotel(Model):
    contact_email = EmailField(verbose_name=_('E-Mail'))
    description = TextField(verbose_name=_('Description'))
    name = CharField(verbose_name=_('Name'), max_length=200)
    url = URLField(verbose_name=_('URL'))

    def __str__(self):
        return self.contact_email


class Room(Model):
    hotel = ForeignKey(Hotel, on_delete=CASCADE, verbose_name=_('Hotel'))
    available_beds = SmallIntegerField(verbose_name=_('Available Beds'))
    coin = CharField(max_length=100, verbose_name=_('Coin'))
    floor = SmallIntegerField(verbose_name=_('Floor'))
    matrimonial = BooleanField(verbose_name=_('Matrimonial'))
    number = CharField(max_length=50, verbose_name=_('Number'))
    price_per_bed = DecimalField(verbose_name=_('Bed`s Prices'), max_digits=6, decimal_places=2) # Arreglar Verbose
    total_beds = SmallIntegerField(verbose_name=_('Total Beds'))

    def __str__(self):
        return self.hotel


class QuestionCategory(Model):
    emoji_alt = CharField(verbose_name=_('Emoji'), max_length=50)
    name = CharField(max_length=100, verbose_name=_('Category'))

    def __str__(self):
        return self.name


class Question(Model):
    category = ForeignKey(QuestionCategory, on_delete=CASCADE)
    answer = TextField(verbose_name=_('Answer'))
    created = DateField(verbose_name=_('Date Created'), auto_now_add=True)
    published = BooleanField(verbose_name=_('Published'))
    question = TextField(verbose_name=_('Question'))

    def __str__(self):
        return self.question


class DateState(Model):
    start_date = models.DateField(verbose_name=_("Period start date"))
    finish_date = models.DateField(verbose_name=_("Period finish date"))

    def __str__(self):
        return 'Periodo'


class Profile(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'))
    name = CharField(max_length=255, verbose_name=_('Name'))
    last_name = CharField(max_length=255, verbose_name=_('Last name'))
    institution = CharField(max_length=12, verbose_name=_('Institution'))
    alimentary_restriction = TextField(verbose_name=_('Food Restriction'), null=True)
    born_date = DateField(verbose_name=_('Born Date'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Gender'))
    health_consideration = TextField(verbose_name=_('Health Considerations'), null=True)
    identification = CharField(max_length=12, verbose_name=_('Identification'), null=True)
    nationality = CharField(max_length=12, verbose_name=_('Nationality'))
    snore = BooleanField(verbose_name=_('Snore?'), default=False)
    enrolled = BooleanField(verbose_name=_('Enrolled?'), default=False)

    # About the likes and the register in the differents activities
    likes = ManyToManyField(Speech, related_name='profile_speech_likes')
    matriculatedspeechs = ManyToManyField(Speech)
    entry_country = IntegerField(verbose_name=_('Entry and out from country'), null=True)
    out_country = IntegerField(verbose_name=_('Entry and otu from country'), null=True)
    entry_port = CharField(max_length=100, verbose_name=_('Entry port'), null=True)
    out_port = CharField(max_length=100, verbose_name=_('Out port'), null=True)
    entry_country_date = DateTimeField(verbose_name=_('Entry country Date'), null=True)
    out_country_date = DateTimeField(verbose_name=_('Out country Date'), null=True)
    letter = TextField(verbose_name=_('Migratory letter'), null=True)

    def save(self, *args, **kwargs):
        periodo = get_active_period()
        if periodo != 0:
            self.enrolled = True
            super(Profile, self).save(*args, **kwargs) # Call the "real" save() method.
        super(Profile, self).save(*args, **kwargs) # Call the "real" save() method.

    def __str__(self):
        return self.user.username


class Patrocinadores(Model):
    name = CharField(max_length=100, verbose_name=_('Name'))
    web = URLField(verbose_name=_('Web'))
    #logo = ImageField(verbose_name=_('logo'), upload_to='logos/')