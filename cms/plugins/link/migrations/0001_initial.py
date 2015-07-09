# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('url', models.URLField(null=True, verbose_name='link', blank=True)),
                ('mailto', models.EmailField(help_text='An email address has priority over a text link.', max_length=75, null=True, verbose_name='email address', blank=True)),
                ('target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[(b'', 'same window'), (b'_blank', 'new window'), (b'_parent', 'parent window'), (b'_top', 'topmost frame')])),
                ('page_link', models.ForeignKey(blank=True, to='cms.Page', help_text='A link to a page has priority over a text link.', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_link',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
