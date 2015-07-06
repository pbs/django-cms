from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.conf import global_settings
from cms.conf.patch import pre_patch, post_patch, post_patch_check


class MenusConfig(AppConfig):
    name = 'menus'
    verbose_name = _("django CMS menus system")

    def ready(self):
        from menus.menu_pool import menu_pool
        menu_pool.discover_menus()