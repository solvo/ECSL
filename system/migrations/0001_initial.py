# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DateState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Period start date')),
                ('finish_date', models.DateField(verbose_name='Period finish date')),
            ],
        ),
        migrations.CreateModel(
            name='djkombu_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(db_index=True, default=True)),
                ('sent_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('payload', models.TextField(verbose_name='payload')),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='djkombu_Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'queue',
                'verbose_name_plural': 'queues',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('description', models.TextField(verbose_name='Description')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mozilla_subvention', models.BooleanField(default=False, verbose_name='Mozilla Subvention?')),
                ('mozilla_subvention_description', models.TextField(verbose_name='Mozilla Subvention Description')),
                ('payed', models.BooleanField(default=False, verbose_name='Payed?')),
                ('not_registered', models.BooleanField(default=False, verbose_name='Not aprove ')),
                ('registered', models.BooleanField(default=False, verbose_name='Aprove')),
                ('subvention_description', models.TextField(verbose_name='Subvention Description')),
                ('subvention_request', models.BooleanField(default=False, verbose_name='Subvention Request')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('web', models.URLField(verbose_name='Web')),
                ('logo', models.ImageField(upload_to='logos/', verbose_name='logo')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('institution', models.CharField(max_length=12, verbose_name='Institution')),
                ('alimentary_restriction', models.TextField(null=True, verbose_name='Food Restriction')),
                ('born_date', models.DateField(verbose_name='Born Date')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Gender')),
                ('health_consideration', models.TextField(null=True, verbose_name='Health Considerations')),
                ('identification', models.CharField(max_length=12, null=True, verbose_name='Identification')),
                ('nationality', models.CharField(max_length=12, verbose_name='Nationality')),
                ('snore', models.BooleanField(default=False, verbose_name='Snore?')),
                ('enrolled', models.BooleanField(default=False, verbose_name='Enrolled?')),
                ('entry_country', models.IntegerField(null=True, verbose_name='Entry and out from country')),
                ('out_country', models.IntegerField(null=True, verbose_name='Entry and otu from country')),
                ('entry_port', models.CharField(max_length=100, null=True, verbose_name='Entry port')),
                ('out_port', models.CharField(max_length=100, null=True, verbose_name='Out port')),
                ('entry_country_date', models.DateTimeField(null=True, verbose_name='Entry country Date')),
                ('out_country_date', models.DateTimeField(null=True, verbose_name='Out country Date')),
                ('letter', models.TextField(null=True, verbose_name='Migratory letter')),
                ('invitation_file', models.BooleanField(default=False, verbose_name='Invitation email')),
                ('diploma', models.BooleanField(default=False, verbose_name='Diploma archivo')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Date Created')),
                ('published', models.BooleanField(verbose_name='Published')),
                ('question', models.TextField(verbose_name='Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji_alt', models.CharField(max_length=50, verbose_name='Emoji')),
                ('name', models.CharField(max_length=100, verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_beds', models.SmallIntegerField(verbose_name='Available Beds')),
                ('coin', models.CharField(max_length=100, verbose_name='Coin')),
                ('floor', models.SmallIntegerField(verbose_name='Floor')),
                ('matrimonial', models.BooleanField(verbose_name='Matrimonial')),
                ('number', models.CharField(max_length=50, verbose_name='Number')),
                ('price_per_bed', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Bed`s Prices')),
                ('total_beds', models.SmallIntegerField(verbose_name='Total Beds')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Hotel', verbose_name='Hotel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audience', models.CharField(choices=[('PG', 'Publico General'), ('NB', 'Nivel Basico'), ('NI', 'Nivel Intermedio'), ('NA', 'Nivel Avanzado'), ('PRO', 'Profesional')], max_length=45, verbose_name='Audience')),
                ('description', models.TextField(verbose_name='Description')),
                ('notes', models.TextField(verbose_name='Notes')),
                ('skill_level', models.PositiveIntegerField(verbose_name='Skill Level')),
                ('speaker_information', models.TextField(verbose_name='Speaker Information')),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('places', models.CharField(max_length=250, null=True, verbose_name='Places')),
                ('days', models.DateTimeField(null=True, verbose_name='Event Start')),
                ('slug', models.SlugField(help_text='Generador de url, se recomienda no modificar', unique=True)),
                ('date_start', models.DateTimeField(null=True, verbose_name='Start Date')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='SpeechType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Talleres', 'Talleres'), ('Charlas', 'Charlas'), ('Dialogos', 'Dialogos')], max_length=45, verbose_name='Name')),
                ('icons', models.CharField(choices=[('/static/img/talleres.png', 'T'), ('/static/img/charlas.png', 'CH'), ('/static/img/dialogos.png', 'D')], max_length=45, verbose_name='Icons')),
                ('slug', models.SlugField(help_text='Generador de url, se recomienda no modificar', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(help_text='Generador de url, se recomienda no modificar', unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Tshirt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(verbose_name='Amount')),
                ('last_update', models.DateField(verbose_name='Last Update')),
                ('size', models.CharField(max_length=15, verbose_name='Size')),
            ],
        ),
        migrations.CreateModel(
            name='TshirtStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Description')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Gender')),
                ('img1', models.ImageField(upload_to='Tshirt/', verbose_name='Image 1')),
                ('img2', models.ImageField(upload_to='Tshirt/', verbose_name='Image 2')),
                ('img3', models.ImageField(upload_to='Tshirt/', verbose_name='Image 3')),
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Price')),
            ],
        ),
        migrations.AddField(
            model_name='tshirt',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.TshirtStyle', verbose_name='Style'),
        ),
        migrations.AddField(
            model_name='tshirt',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='speech',
            name='speech_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.SpeechType', verbose_name='Speech Type'),
        ),
        migrations.AddField(
            model_name='speech',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='speech',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.QuestionCategory'),
        ),
        migrations.AddField(
            model_name='profile',
            name='likes',
            field=models.ManyToManyField(related_name='profile_speech_likes', to='system.Speech'),
        ),
        migrations.AddField(
            model_name='profile',
            name='matriculatedspeechs',
            field=models.ManyToManyField(to='system.Speech'),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='djkombu_message',
            name='queue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='system.djkombu_Queue'),
        ),
    ]
