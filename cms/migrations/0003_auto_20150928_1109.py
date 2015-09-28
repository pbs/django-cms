# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_update_template_field'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='pageuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='cmsplugin',
            name='plugin_type',
            field=models.CharField(verbose_name='plugin_name', max_length=50, editable=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='globalpagepermission',
            name='sites',
            field=models.ManyToManyField(help_text='If none selected, user haves granted permissions to all sites.', to='sites.Site', verbose_name='sites', blank=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='moderator_state',
            field=models.SmallIntegerField(default=1, blank=True, verbose_name='moderator state', choices=[(0, 'changed'), (1, 'req. app.'), (2, 'delete'), (10, 'approved'), (11, 'app. par.')]),
        ),
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(help_text='The template used to render the content.', max_length=100, verbose_name='template', choices=[(b'test-template.html', 'Test Template')]),
        ),
        migrations.AlterField(
            model_name='pagemoderatorstate',
            name='action',
            field=models.CharField(blank=True, max_length=3, null=True, choices=[(b'ADD', 'created'), (b'CHA', 'changed'), (b'DEL', 'delete req.'), (b'MOV', 'move req.'), (b'PUB', 'publish req.'), (b'UNP', 'unpublish req.'), (b'APP', 'approved')]),
        ),
        migrations.AlterField(
            model_name='title',
            name='has_url_overwrite',
            field=models.BooleanField(default=False, verbose_name='has url overwrite', db_index=True, editable=False),
        ),
    ]
