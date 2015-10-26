# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.core import paginator

class ObjectCachedPaginator(paginator.Paginator):
    """
        Custom paginator that will cache pages per page number
        for a paginator instance.
    """

    def page(self, number):
        if not hasattr(self, '_page_%d' % number):
            setattr(self, '_page_%d' % number,
                    super(ObjectCachedPaginator, self).page(number))
        return getattr(self, '_page_%d' % number)


class CMSSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            self._paginator = ObjectCachedPaginator(self.items(), self.limit)
        return self._paginator

    def items(self):
        from cms.utils.moderator import get_page_queryset
        page_queryset = get_page_queryset(None)
        all_pages = page_queryset.published().filter(login_required=False)
        # page is 1 by default for get_urls method
        page = 1
        # iterate through cms pages and set homepage when found in order
        #   to not execute expensive queries just to re-fetch it for
        #   each root page
        homepage_pk = None
        for page in all_pages:
            if not homepage_pk:
                if page.is_home():
                    homepage_pk = page.pk
                else:
                    page.home_pk_cache = homepage_pk
        return all_pages

    def lastmod(self, page):
        from cms.models import CMSPlugin
        mod_dates = [page.changed_date, page.publication_date]
        latest_plg = CMSPlugin.objects.filter(
            placeholder__page=page).only('changed_date').order_by(
            '-changed_date')[:1]

        if latest_plg:
            mod_dates.append(latest_plg[0].changed_date)
        return max(mod_dates)

