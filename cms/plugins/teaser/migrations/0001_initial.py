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
            name='Teaser',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('image', models.ImageField(upload_to=cms.models.pluginmodel.get_plugin_media_path, null=True, verbose_name='image', blank=True)),
                ('url', models.CharField(help_text='If present image will be clickable.', max_length=255, null=True, verbose_name='link', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='If present image will be clickable', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_teaser',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
