# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_bentolayout_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bentolayout',
            name='image',
        ),
    ]
