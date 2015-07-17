# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields
from django.conf import settings
import cms.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSPlugin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.PositiveSmallIntegerField(verbose_name='position', null=True, editable=False, blank=True)),
                ('language', models.CharField(verbose_name='language', max_length=15, editable=False, db_index=True)),
                ('plugin_type', models.CharField(verbose_name='plugin name', max_length=50, editable=False, db_index=True)),
                ('creation_date', models.DateTimeField(default=cms.utils.timezone.now, verbose_name='creation date', editable=False)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', models.ForeignKey(blank=True, editable=False, to='cms.CMSPlugin', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GlobalPagePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_change', models.BooleanField(default=True, verbose_name='can edit')),
                ('can_add', models.BooleanField(default=True, verbose_name='can add')),
                ('can_delete', models.BooleanField(default=True, verbose_name='can delete')),
                ('can_change_advanced_settings', models.BooleanField(default=False, verbose_name='can change advanced settings')),
                ('can_publish', models.BooleanField(default=True, verbose_name='can publish')),
                ('can_set_navigation', models.BooleanField(default=True, verbose_name='can set navigation')),
                ('can_change_permissions', models.BooleanField(default=False, help_text='on page level', verbose_name='can change permissions')),
                ('can_move_page', models.BooleanField(default=True, verbose_name='can move')),
                ('can_moderate', models.BooleanField(default=True, verbose_name='can moderate')),
                ('can_view', models.BooleanField(default=False, help_text='frontend view restriction', verbose_name='view restricted')),
                ('can_recover_page', models.BooleanField(default=True, help_text='can recover any deleted page', verbose_name='can recover pages')),
            ],
            options={
                'verbose_name': 'Page global permission',
                'verbose_name_plural': 'Pages global permissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_by', models.CharField(verbose_name='created by', max_length=70, editable=False)),
                ('changed_by', models.CharField(verbose_name='changed by', max_length=70, editable=False)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('changed_date', models.DateTimeField(auto_now=True)),
                ('publication_date', models.DateTimeField(help_text='When the page should go live. Status must be "Published" for page to go live.', null=True, verbose_name='publication date', db_index=True, blank=True)),
                ('publication_end_date', models.DateTimeField(help_text='When to expire the page. Leave empty to never expire.', null=True, verbose_name='publication end date', db_index=True, blank=True)),
                ('in_navigation', models.BooleanField(default=True, db_index=True, verbose_name='in navigation')),
                ('soft_root', models.BooleanField(default=False, help_text='All ancestors will not be displayed in the navigation', db_index=True, verbose_name='soft root')),
                ('reverse_id', models.CharField(max_length=40, blank=True, help_text='An unique identifier that is used with the page_url templatetag for linking to this page', null=True, verbose_name='id', db_index=True)),
                ('navigation_extenders', models.CharField(db_index=True, max_length=80, null=True, verbose_name='attached menu', blank=True)),
                ('published', models.BooleanField(default=False, verbose_name='is published')),
                ('template', models.CharField(help_text='The template used to render the content.', max_length=100, verbose_name='template', choices=[(b'test-template.html', 'Test Template')])),
                ('moderator_state', models.SmallIntegerField(default=1, blank=True, verbose_name='moderator state', choices=[(0, 'changed'), (1, 'approval required'), (2, 'delete'), (10, 'approved'), (11, 'app. par.')])),
                ('login_required', models.BooleanField(default=False, verbose_name='login required')),
                ('limit_visibility_in_menu', models.SmallIntegerField(default=None, choices=[(1, 'for logged in users only'), (2, 'for anonymous users only')], blank=True, help_text='limit when this page is visible in the menu', null=True, verbose_name='menu visibility', db_index=True)),
                ('publisher_is_draft', models.BooleanField(default=1, db_index=True, editable=False)),
                ('publisher_state', models.SmallIntegerField(default=0, editable=False, db_index=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='cms.Page', null=True)),
            ],
            options={
                'ordering': ('site', 'tree_id', 'lft'),
                'verbose_name': 'page',
                'verbose_name_plural': 'pages',
                'permissions': (('view_page', 'Can view page'),),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageModerator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('moderate_page', models.BooleanField(default=False, verbose_name='Moderate page')),
                ('moderate_children', models.BooleanField(default=False, verbose_name='Moderate children')),
                ('moderate_descendants', models.BooleanField(default=False, verbose_name='Moderate descendants')),
                ('page', models.ForeignKey(verbose_name='Page', to='cms.Page')),
            ],
            options={
                'verbose_name': 'PageModerator',
                'verbose_name_plural': 'PageModerator',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageModeratorState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(blank=True, max_length=3, null=True, choices=[(b'ADD', 'created'), (b'CHA', 'changed'), (b'DEL', 'deletion request'), (b'MOV', 'move request'), (b'PUB', 'publish request'), (b'UNP', 'unpublish request'), (b'APP', 'approved')])),
                ('message', models.TextField(default=b'', max_length=1000, blank=True)),
                ('page', models.ForeignKey(to='cms.Page')),
            ],
            options={
                'ordering': ('page', 'action', '-created'),
                'verbose_name': 'Page moderator state',
                'verbose_name_plural': 'Page moderator states',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PagePermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('can_change', models.BooleanField(default=True, verbose_name='can edit')),
                ('can_add', models.BooleanField(default=True, verbose_name='can add')),
                ('can_delete', models.BooleanField(default=True, verbose_name='can delete')),
                ('can_change_advanced_settings', models.BooleanField(default=False, verbose_name='can change advanced settings')),
                ('can_publish', models.BooleanField(default=True, verbose_name='can publish')),
                ('can_set_navigation', models.BooleanField(default=True, verbose_name='can set navigation')),
                ('can_change_permissions', models.BooleanField(default=False, help_text='on page level', verbose_name='can change permissions')),
                ('can_move_page', models.BooleanField(default=True, verbose_name='can move')),
                ('can_moderate', models.BooleanField(default=True, verbose_name='can moderate')),
                ('can_view', models.BooleanField(default=False, help_text='frontend view restriction', verbose_name='view restricted')),
                ('grant_on', models.IntegerField(default=5, verbose_name='Grant on', choices=[(1, 'Current page'), (2, 'Page children (immediate)'), (3, 'Page and children (immediate)'), (4, 'Page descendants'), (5, 'Page and descendants')])),
            ],
            options={
                'verbose_name': 'Page permission',
                'verbose_name_plural': 'Page permissions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PageUser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='created_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User (page)',
                'verbose_name_plural': 'Users (page)',
            },
            bases=('auth.user',),
        ),
        migrations.CreateModel(
            name='PageUserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='auth.Group')),
                ('created_by', models.ForeignKey(related_name='created_usergroups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User group (page)',
                'verbose_name_plural': 'User groups (page)',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slot', models.CharField(verbose_name='slot', max_length=50, editable=False, db_index=True)),
                ('default_width', models.PositiveSmallIntegerField(verbose_name='width', null=True, editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=15, verbose_name='language', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('menu_title', models.CharField(help_text='overwrite the title in the menu', max_length=255, null=True, verbose_name='title', blank=True)),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('path', models.CharField(max_length=255, verbose_name='Path', db_index=True)),
                ('has_url_overwrite', models.BooleanField(default=False, verbose_name='has URL overwrite', db_index=True, editable=False)),
                ('application_urls', models.CharField(db_index=True, max_length=200, null=True, verbose_name='application', blank=True)),
                ('redirect', models.CharField(max_length=255, null=True, verbose_name='redirect', blank=True)),
                ('meta_description', models.TextField(max_length=255, null=True, verbose_name='description', blank=True)),
                ('meta_keywords', models.CharField(max_length=255, null=True, verbose_name='keywords', blank=True)),
                ('page_title', models.CharField(help_text='overwrite the title (html title tag)', max_length=255, null=True, verbose_name='title', blank=True)),
                ('creation_date', models.DateTimeField(default=cms.utils.timezone.now, verbose_name='creation date', editable=False)),
                ('page', models.ForeignKey(related_name='title_set', verbose_name='page', to='cms.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='title',
            unique_together=set([('language', 'page')]),
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='group',
            field=models.ForeignKey(verbose_name='group', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='page',
            field=models.ForeignKey(verbose_name='page', blank=True, to='cms.Page', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagepermission',
            name='user',
            field=models.ForeignKey(verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagemoderatorstate',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagemoderator',
            name='user',
            field=models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='placeholders',
            field=models.ManyToManyField(to='cms.Placeholder', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='publisher_public',
            field=models.OneToOneField(related_name='publisher_draft', null=True, editable=False, to='cms.Page'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(verbose_name='site', to='sites.Site', help_text='The site the page is accessible at.'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='group',
            field=models.ForeignKey(verbose_name='group', blank=True, to='auth.Group', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='sites',
            field=models.ManyToManyField(help_text='If none selected, user haves granted permissions to all sites.', to='sites.Site', null=True, verbose_name='sites', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='globalpagepermission',
            name='user',
            field=models.ForeignKey(verbose_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cmsplugin',
            name='placeholder',
            field=models.ForeignKey(editable=False, to='cms.Placeholder', null=True),
            preserve_default=True,
        ),
    ]
