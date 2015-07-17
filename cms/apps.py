from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from cms.conf import global_settings
from cms.conf.patch import pre_patch, post_patch, post_patch_check


class CMSConfig(AppConfig):
    name = 'cms'
    verbose_name = _("django CMS")

    def __init__(self, *args, **kwargs):
        ret = super(CMSConfig, self).__init__(*args, **kwargs)
        # patch settings
        pre_patch()
        # merge with global cms settings
        for attr in dir(global_settings):
            if attr == attr.upper() and not hasattr(settings, attr):
                setattr(settings._wrapped, attr, getattr(global_settings, attr))
        return ret

    def ready(self):
        post_patch()
        if settings.DEBUG:
            # check if settings are correct, call this only if debugging is enabled
            post_patch_check()

        from cms.plugin_pool import plugin_pool
        plugin_pool.discover_plugins()