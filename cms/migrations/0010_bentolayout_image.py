# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_remove_bentolayout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bentolayout',
            name='image',
            field=models.CharField(max_length=400, blank=True),
        ),
    ]
