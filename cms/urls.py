# -*- coding: utf-8 -*-
from cms.apphook_pool import apphook_pool
from cms.views import details, plugin_to_json, edit_snippet, render_snippet
from django.conf import settings
from django.conf.urls import url, patterns

if settings.APPEND_SLASH:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', details, name='pages-details-by-slug')
else:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)$', details, name='pages-details-by-slug')

urlpatterns = [
    # Public pages
    url(r'^test/plugin_to_json/(?P<plugin_id>.+)/$', plugin_to_json),
    url(r'^test/edit/(?P<ss_id>.+)/$', edit_snippet),
    url(r'^test/render/(?P<snippet_id>.+)/$', render_snippet),
    url(r'^$', details, {'slug':''}, name='pages-root'),
    reg,
]

if apphook_pool.get_apphooks():
    """If there are some application urls, add special resolver, so we will
    have standard reverse support.
    """
    from cms.appresolver import get_app_patterns
    urlpatterns = get_app_patterns() + urlpatterns
    #urlpatterns = (dynamic_app_regex_url_resolver, ) + urlpatterns

urlpatterns = patterns('', *urlpatterns)
