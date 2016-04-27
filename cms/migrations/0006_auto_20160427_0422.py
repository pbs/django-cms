# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_bentolayout_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bentopage',
            name='layout',
        ),
        migrations.AddField(
            model_name='bentopage',
            name='config',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
