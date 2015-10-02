# -*- coding: utf-8 -*-
from django.contrib.sitemaps import Sitemap
from django.core import paginator
from django.db import connection

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
        mod_dates = [page.changed_date, page.publication_date]
        latest_plg_mod_date = None
        with connection.cursor() as cursor:
            cursor.execute(
                "select cmsplg.changed_date from cms_cmsplugin cmsplg " +
                "inner join cms_page_placeholders cmsp " +
                "on cmsp.id=cmsplg.placeholder_id " +
                "where cmsp.page_id = %s " +
                "order by cmsplg.changed_date desc limit 1", [page.id])
            latest_plg_mod_date = cursor.fetchone()

        if latest_plg_mod_date:
            mod_dates.append(latest_plg_mod_date[0])
        return max(mod_dates)

