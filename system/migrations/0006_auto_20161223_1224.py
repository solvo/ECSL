# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-23 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20161223_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tshirtstyle',
            name='img1',
            field=models.ImageField(upload_to='Tshirt/', verbose_name='Image 1'),
        ),
        migrations.AlterField(
            model_name='tshirtstyle',
            name='img2',
            field=models.ImageField(upload_to='Tshirt/', verbose_name='Image 2'),
        ),
        migrations.AlterField(
            model_name='tshirtstyle',
            name='img3',
            field=models.ImageField(upload_to='Tshirt/', verbose_name='Image 3'),
        ),
    ]
