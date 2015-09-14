# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_newsplus', '0002_auto_20150428_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='slug',
            field=models.SlugField(help_text='A slug is a short name which uniquely identifies the news item for this day', unique_for_date='pub_date', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='newsimage',
            name='image',
            field=models.ImageField(upload_to='news_images'),
        ),
    ]
