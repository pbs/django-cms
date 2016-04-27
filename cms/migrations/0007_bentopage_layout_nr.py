# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20160427_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='bentopage',
            name='layout_nr',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
