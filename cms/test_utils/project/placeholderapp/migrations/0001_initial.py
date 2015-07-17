# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields


class Migration(migrations.Migration):

    operations = [
        migrations.CreateModel(
            name='Example1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_1', models.CharField(max_length=255, verbose_name='char_1')),
                ('char_2', models.CharField(max_length=255, verbose_name='char_2')),
                ('char_3', models.CharField(max_length=255, verbose_name='char_3')),
                ('char_4', models.CharField(max_length=255, verbose_name='char_4')),
                ('placeholder', cms.models.fields.PlaceholderField(to='cms.Placeholder', null=True, slotname=b'placeholder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Example2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_1', models.CharField(max_length=255, verbose_name='char_1')),
                ('char_2', models.CharField(max_length=255, verbose_name='char_2')),
                ('char_3', models.CharField(max_length=255, verbose_name='char_3')),
                ('char_4', models.CharField(max_length=255, verbose_name='char_4')),
                ('placeholder', cms.models.fields.PlaceholderField(to='cms.Placeholder', null=True, slotname=b'placeholder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Example3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_1', models.CharField(max_length=255, verbose_name='char_1')),
                ('char_2', models.CharField(max_length=255, verbose_name='char_2')),
                ('char_3', models.CharField(max_length=255, verbose_name='char_3')),
                ('char_4', models.CharField(max_length=255, verbose_name='char_4')),
                ('placeholder', cms.models.fields.PlaceholderField(to='cms.Placeholder', null=True, slotname=b'placeholder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Example4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_1', models.CharField(max_length=255, verbose_name='char_1')),
                ('char_2', models.CharField(max_length=255, verbose_name='char_2')),
                ('char_3', models.CharField(max_length=255, verbose_name='char_3')),
                ('char_4', models.CharField(max_length=255, verbose_name='char_4')),
                ('placeholder', cms.models.fields.PlaceholderField(to='cms.Placeholder', null=True, slotname=b'placeholder')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Example5',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('char_1', models.CharField(max_length=255, verbose_name='char_1')),
                ('char_2', models.CharField(max_length=255, verbose_name='char_2')),
                ('char_3', models.CharField(max_length=255, verbose_name='char_3')),
                ('char_4', models.CharField(max_length=255, verbose_name='char_4')),
                ('placeholder_1', cms.models.fields.PlaceholderField(related_name='p1', slotname=b'placeholder_1', to='cms.Placeholder', null=True)),
                ('placeholder_2', cms.models.fields.PlaceholderField(related_name='p2', slotname=b'placeholder_2', to='cms.Placeholder', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
