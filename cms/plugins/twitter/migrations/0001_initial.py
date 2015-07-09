# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterRecentEntries',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=75, verbose_name='title', blank=True)),
                ('twitter_user', models.CharField(max_length=75, verbose_name='twitter user')),
                ('count', models.PositiveSmallIntegerField(default=3, help_text='Number of entries to display', verbose_name='count')),
                ('link_hint', models.CharField(help_text='If given, the hint is displayed as link to your Twitter profile.', max_length=75, verbose_name='link hint', blank=True)),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_twitterrecententries',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TwitterSearch',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=75, verbose_name='title', blank=True)),
                ('query', models.CharField(default=b'', help_text='Example: "brains AND zombies AND from:umbrella AND to:nemesis": tweets from the user "umbrella" to the user "nemesis" that contain the words "brains" and "zombies"', max_length=200, verbose_name='query', blank=True)),
                ('count', models.PositiveSmallIntegerField(default=3, help_text='Number of entries to display', verbose_name='count')),
            ],
            options={
                'abstract': False,
                'db_table': 'cmsplugin_twittersearch',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
