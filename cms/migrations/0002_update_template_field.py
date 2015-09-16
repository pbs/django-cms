# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(help_text='Templates are used to render the layout of a page.', max_length=100, verbose_name='template', choices=[(b'test-template.html', 'Test Template')]),
            preserve_default=True,
        ),
    ]
