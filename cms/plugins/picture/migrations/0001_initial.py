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
            name='Picture',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='image')),
                ('url', models.CharField(help_text='if present image will be clickable', max_length=255, null=True, verbose_name='link', blank=True)),
                ('alt', models.CharField(help_text='textual description of the image', max_length=255, null=True, verbose_name='alternate text', blank=True)),
                ('longdesc', models.CharField(help_text='additional description of the image', max_length=255, null=True, verbose_name='long description', blank=True)),
                ('float', models.CharField(blank=True, max_length=10, null=True, verbose_name='side', choices=[(b'center', 'center'), (b'left', 'left'), (b'right', 'right')])),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='if present image will be clickable', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_picture',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
