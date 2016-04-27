# -*- coding: utf-8 -*-
from cms.apphook_pool import apphook_pool
from cms.views import details, get_plugins, page_search, add_container, remove_container
from django.conf import settings
from django.conf.urls import url, patterns

if settings.APPEND_SLASH:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', details, name='pages-details-by-slug')
else:
    reg = url(r'^(?P<slug>[0-9A-Za-z-_.//]+)$', details, name='pages-details-by-slug')

urlpatterns = [
    # Public pages
    url(r'^new/getplugins/(?P<width>\d+)/(?P<height>\d+)', get_plugins),
    url(r'^new/search/(?P<search_text>.+)', page_search),
    url(r'^new/addcontainer/(?P<page_id>\d+)/(?P<container_type>.+)', add_container),
    url(r'^new/removecontainer/(?P<page_id>\d+)/(?P<container_id>\d+)', remove_container),
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
