# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20150928_1109'),
    ]

    operations = [
        migrations.CreateModel(
            name='BentoLayout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stuff', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='BentoPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('layout', models.ForeignKey(to='cms.BentoLayout')),
            ],
        ),
    ]
