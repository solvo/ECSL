# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 09:44
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
                ('mozilla_subvention', models.BooleanField(verbose_name='Mozilla Subvention?')),
                ('mozilla_subvention_description', models.TextField(verbose_name='Mozilla Subvention Description')),
                ('payed', models.BooleanField(verbose_name='Payed?')),
                ('preregistered', models.BooleanField(verbose_name='Preregistered')),
                ('registered', models.BooleanField(verbose_name='Registered')),
                ('subvention_description', models.TextField(verbose_name='Subvention Description')),
                ('subvention_request', models.BooleanField(verbose_name='Subvention Request')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('alimentary_restriction', models.TextField(null=True, verbose_name='Food Restriction')),
                ('born_date', models.DateField(verbose_name='Born Date')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1, verbose_name='Gender')),
                ('health_consideration', models.TextField(null=True, verbose_name='Health Considerations')),
                ('identification', models.CharField(max_length=12, null=True, verbose_name='Identification')),
                ('institution', models.CharField(max_length=12, verbose_name='Institution')),
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
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('created', models.DateField(verbose_name='Date Created')),
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
                ('title', models.TextField(verbose_name='Title')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeechType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Talleres', 'T'), ('Charlas', 'CH'), ('Dialogos', 'D')], max_length=45, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('slug', models.SlugField(unique=True)),
            ],
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
                ('name', models.CharField(max_length=45, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Image 1')),
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
    ]
