# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('djangocms_blog', '0012_auto_20151220_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='main_image',
            field=filer.fields.image.FilerImageField(related_name='djangocms_blog_category_image', on_delete=django.db.models.deletion.SET_NULL, verbose_name='main image', blank=True, to='filer.Image', null=True),
        ),
    ]
