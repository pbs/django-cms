# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='mailto',
            field=models.EmailField(help_text='An email adress has priority over a text link.', max_length=254, null=True, verbose_name='mailto', blank=True),
        ),
    ]
