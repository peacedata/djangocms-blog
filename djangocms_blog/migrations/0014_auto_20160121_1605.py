# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_vimeo.fields
import filer.fields.image
import django.db.models.deletion
import django_vimeo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('djangocms_blog', '0013_blogcategory_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='main_video',
            field=django_vimeo.fields.VimeoField(storage=django_vimeo.storage.VimeoFileStorage(), upload_to=b'', null=True, verbose_name='main video', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='main_video_poster',
            field=filer.fields.image.FilerImageField(related_name='djangocms_blog_post_video_poster', on_delete=django.db.models.deletion.SET_NULL, verbose_name='main video poster', blank=True, to='filer.Image', null=True),
        ),
    ]
