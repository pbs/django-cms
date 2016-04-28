# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pagemodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_bentopage_layout_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='bentolayout',
            name='image',
            field=models.ImageField(upload_to=cms.models.pagemodel.get_plugin_media_path, verbose_name='image', blank=True),
        ),
    ]
