# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flash',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('file', models.FileField(help_text='use swf file', upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='file')),
                ('width', models.CharField(max_length=6, verbose_name='width')),
                ('height', models.CharField(max_length=6, verbose_name='height')),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_flash'
            },
            bases=('cms.cmsplugin',),
        ),
    ]
