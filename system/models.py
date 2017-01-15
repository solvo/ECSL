# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings


def get_active_period():
    period = DateState.objects.filter(start_date__lte=now(), finish_date__gte=now())
    if period.exists():
        return period.last()
    return 0


class Inscription(Model):
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    mozilla_subvention_description = TextField(verbose_name=_('Mozilla Descripción Propuesta'))
    payed = BooleanField(verbose_name=_('¿Pagado?'), default=False)
    not_registered = BooleanField(verbose_name=_('No aprobado'), default=False)
    registered = BooleanField(verbose_name=_('Aprobado'), default=False)
    subvention_request = BooleanField(verbose_name=_('¿Propuesta Enviada?'), default=False)

    def __str__(self):
        return self.user.username


class TshirtStyle(Model):

    description = TextField(verbose_name=_('Descripción'))
    img1 = ImageField(verbose_name=_('Imagen 1'), upload_to='Tshirt/')
    img2 = ImageField(verbose_name=_('Imagen 2'), upload_to='Tshirt/')
    img3 = ImageField(verbose_name=_('Imagen 3'), upload_to='Tshirt/')
    name = CharField(max_length=45, verbose_name=_('Nombre'))
    price = DecimalField(verbose_name=_('Precio'), decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name


class Tshirt(Model):
    gender_choice = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino')
    )
    gender = CharField(max_length=9, choices=gender_choice, verbose_name=_('Género'), default='Masculino')
    style = ForeignKey(TshirtStyle, on_delete=CASCADE, verbose_name=_('Estilo'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    amount = PositiveIntegerField(verbose_name=_('Cantidad'))
    last_update = DateField(verbose_name=_('Última Actualización'))
    size = CharField(max_length=15, verbose_name=_('Talla'))
    pagada = BooleanField(default=False)

    def __str__(self):
        return self.style.name + ' ' + self.style.description


class SpeechType(Model):
    speech_choice = (
        ('Talleres', 'Talleres'),
        ('Charlas', 'Charlas'),
        ('Diálogos', 'Diálogos')
    )

    speech_icons = (
        (settings.STATIC_URL + 'img/talleres.png', 'Talleres'),
        (settings.STATIC_URL + 'img/charlas.png', 'Charlas'),
        (settings.STATIC_URL + 'img/dialogos.png', 'Diálogos')
    )

    name = CharField(max_length=45, verbose_name=_('Nombre'), choices=speech_choice)
    icons = CharField(max_length=45, verbose_name=_('Iconos'), choices=speech_icons)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')

    def __str__(self):
        return self.name


class Topic(Model):

    name = CharField(max_length=45, verbose_name=_('Nombre'),unique=True)
    description = TextField(verbose_name=_('Descripción'))
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar')
    date_created = DateTimeField(verbose_name=_('Fecha de Creado'), auto_now_add=True)

    class Meta:
        ordering = ["-date_created"]

    def __str__(self):
        return self.slug


class Speech(Model):

    class Meta:
        ordering = ["date_created"]

    speech_audience = (
        ('PG', 'Público General'),
        ('NB', 'Nivel Basico'),
        ('NI', 'Nivel Intermedio'),
        ('NA', 'Nivel Avanzado'),
        ('PRO', 'Profesional'),
    )

    speech_type = ForeignKey(SpeechType, verbose_name=_('Tipo de Actividad'))
    topic = ForeignKey(Topic, verbose_name=_('Tema'))
    user = ForeignKey(User, on_delete=CASCADE, related_name='speechs', verbose_name=_('Usuario'))
    audience = CharField(verbose_name=_('Público'), choices=speech_audience, max_length=45)
    description = TextField(verbose_name=_('Descripción'))
    notes = TextField(verbose_name=_('Notas'))
    skill_level = PositiveIntegerField(verbose_name=_('Nivel de Habilidad'))
    speaker_information = TextField(verbose_name=_('Información del Autor'))
    title = CharField(max_length=250, verbose_name=_('Título'))
    places = CharField(max_length=250, verbose_name=_('Lugares'), null=True)
    pepe = DateTimeField(verbose_name=_('Fecha del Evento'), null=True)
    slug = SlugField(unique=True, help_text='Generador de url, se recomienda no modificar', max_length=255)
    date_created = DateTimeField(verbose_name=_('Fecha de Creado'), auto_now_add=True)
    published = BooleanField(verbose_name=_('¿Publicado?'), default=False)

    def __str__(self):
        return self.speech_type.name + ' de ' + self.topic.name

    def cantidad_de_likes(self):
        likes = self.profile_speech_likes.all()
        return likes.count()


class Hotel(Model):
    contact_email = EmailField(verbose_name=_('E-Mail'))
    description = TextField(verbose_name=_('Descripción'))
    name = CharField(verbose_name=_('Nombre'), max_length=200)
    url = URLField(verbose_name=_('URL'))

    def __str__(self):
        return self.contact_email


class Room(Model):
    hotel = ForeignKey(Hotel, on_delete=CASCADE, verbose_name=_('Hotel'))
    user = ForeignKey(User, on_delete=CASCADE, verbose_name=_('Usuario'))
    available_beds = SmallIntegerField(verbose_name=_('Camas Disponibles'))
    coin = CharField(max_length=100, verbose_name=_('Moneda'))
    floor = SmallIntegerField(verbose_name=_('Piso'))
    matrimonial = BooleanField(verbose_name=_('Matrimonial'))
    number = CharField(max_length=50, verbose_name=_('Número'))
    price_per_bed = DecimalField(verbose_name=_('Precio de la Cama'), max_digits=6, decimal_places=2) # Arreglar Verbose
    total_beds = SmallIntegerField(verbose_name=_('Total de Camas'))

    def __str__(self):
        return self.hotel.name


class QuestionCategory(Model):
    emoji_alt = CharField(verbose_name=_('Emoji'), max_length=50)
    name = CharField(max_length=100, verbose_name=_('Categoría'))

    def __str__(self):
        return self.name


class Question(Model):
    category = ForeignKey(QuestionCategory, on_delete=CASCADE)
    answer = TextField(verbose_name=_('Respuestas'))
    created = DateField(verbose_name=_('Fecha de Creación'), auto_now_add=True)
    published = BooleanField(verbose_name=_('¿Publicado?'))
    question = TextField(verbose_name=_('Pregunta'))

    def __str__(self):
        return self.question


class DateState(Model):
    start_date = models.DateField(verbose_name=_("Fecha de Inicio"))
    finish_date = models.DateField(verbose_name=_("Fecha de Conclusión"))

    def __str__(self):
        return 'Tiempo Registro'


class Profile(Model):
    gender_choice = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    user = OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))
    name = CharField(max_length=255, verbose_name=_('Nombre'))
    last_name = CharField(max_length=255, verbose_name=_('Apellido'))
    institution = CharField(max_length=12, verbose_name=_('Institución'))
    alimentary_restriction = TextField(verbose_name=_('Restrinción Alimentaria'), null=True)
    born_date = DateField(verbose_name=_('Fecha de Nacimiento'))
    gender = CharField(max_length=1, choices=gender_choice, verbose_name=_('Genero'))
    health_consideration = TextField(verbose_name=_('Condiciones de Salud'), null=True)
    identification = CharField(max_length=12, verbose_name=_('Identificación'), null=True)
    nationality = CharField(max_length=12, verbose_name=_('Nacionalidad'))
    snore = BooleanField(verbose_name=_('¿Ronca?'), default=False)
    enrolled = BooleanField(verbose_name=_('¿Matriculado?'), default=False)

    # About the likes and the register in the differents activities
    likes = ManyToManyField(Speech, related_name='profile_speech_likes', blank=True)
    matriculatedspeechs = ManyToManyField(Speech, blank=True)
    entry_country = IntegerField(verbose_name=_('Entradas del País'), null=True)
    out_country = IntegerField(verbose_name=_('Salidas del País'), null=True)
    entry_port = CharField(max_length=100, verbose_name=_('Puerto de Entrada'), null=True)
    out_port = CharField(max_length=100, verbose_name=_('Puerto de Salida'), null=True)
    entry_country_date = DateField(verbose_name=_('Fecha de Entrada al país'), null=True)
    out_country_date = DateField(verbose_name=_('Fecha de Salida del país'), null=True)
    letter = TextField(verbose_name=_('Carta Migratoria'), null=True)
    invitation_file = BooleanField(verbose_name=_('¿Email de Invitación?'), default=False)
    diploma = BooleanField(verbose_name=_('¿Email de Diploma?'), default=False)

    def save(self, *args, **kwargs):
        periodo = get_active_period()
        if periodo != 0:
            self.enrolled = True
            super(Profile, self).save(*args, **kwargs)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

    def camisetas_sin_pagar(self):
        camisetas = Tshirt.objects.filter(user=self.user, pagada=False)
        return camisetas.count()


class Matriculado(Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    speech = models.ForeignKey(Speech, on_delete=models.CASCADE)
    # para el tema de los 10 min de antelacion
    avisado = models.BooleanField(default=False)


class Patrocinadores(Model):
    name = CharField(max_length=100, verbose_name=_('Nombre'))
    web = URLField(verbose_name=_('Web'))
    logo = ImageField(verbose_name=_('logo'), upload_to='logos/')


class SpeechResource(Model):
    speech = ForeignKey(Speech, related_name='recursos')
    recurso = FileField(upload_to='recursos/')

    def nombre(self):
        direccion = self.recurso.name
        nombre = direccion.split('/').pop()
        return nombre

    def get_absolute_url(self):
        return '/activity/' + self.speech.topic.slug + "/" + self.speech.slug

# from djkombu.managers import QueueManager, MessageManager
#
#
# class djkombu_Queue(models.Model):
#     name = models.CharField(_("name"), max_length=200, unique=True)
#
#     objects = QueueManager()
#
#     class Meta:
#         verbose_name = _("queue")
#         verbose_name_plural = _("queues")
#
#
# class djkombu_Message(models.Model):
#     visible = models.BooleanField(default=True, db_index=True)
#     sent_at = models.DateTimeField(null=True, blank=True, db_index=True,
#                 auto_now_add=True)
#     payload = models.TextField(_("payload"), null=False)
#     queue = models.ForeignKey(djkombu_Queue, related_name="messages")
#
#     objects = MessageManager()
#
#     class Meta:
#         verbose_name = _("message")
#         verbose_name_plural = _("messages")
