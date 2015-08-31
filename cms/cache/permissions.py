# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.cache import cache

from django.contrib.auth.models import User

from cms.conf import global_settings

PERMISSION_KEYS = [
    'can_change', 'can_add', 'can_delete',
    'can_change_advanced_settings', 'can_publish', 'can_set_navigation',
    'can_change_permissions', 'can_move_page',
    'can_moderate', 'can_view']


def get_cache_key(user, key):
    # To optimize the ammout of data returned from the db, this can also be used only with
    # the username. Previous usage (with the full user) has been left for compatibility.
    username = user.username if hasattr(user, 'username') else user
    return "%s:permission:%s:%s" % (
        settings.CMS_CACHE_PREFIX, username, key)


def get_permission_cache(user, key):
    """
    Helper for reading values from cache
    """
    return cache.get(get_cache_key(user, key))


def set_permission_cache(user, key, value):
    """
    Helper method for storing values in cache. Stores used keys so
    all of them can be cleaned when clean_permission_cache gets called.
    """
    # store this key, so we can clean it when required
    cache_key = get_cache_key(user, key)
    cache.set(cache_key, value, settings.CMS_CACHE_DURATIONS['permissions'])


def clear_user_permission_cache(user):
    """
    Cleans permission cache for given user.
    """
    if global_settings.CMS_DISABLE_SITE_CACHE_CLEAR:
        # Cache clearing is temporarily disabled, see
        # global_settings.CMS_DISABLE_SITE_CACHE_CLEAR for more info.
        return
    for key in PERMISSION_KEYS:
        cache.delete(get_cache_key(user, key))


def clear_permission_cache():
    if global_settings.CMS_DISABLE_SITE_CACHE_CLEAR:
        # Cache clearing is temporarily disabled, see
        # global_settings.CMS_DISABLE_SITE_CACHE_CLEAR for more info.
        return
    usernames = User.objects.filter(is_active=True).values_list('username', flat=True)
    cache_keys_to_delete = []
    for username in usernames:
        for key in PERMISSION_KEYS:
            cache_keys_to_delete.append(get_cache_key(username, key))
    cache.delete_many(cache_keys_to_delete)
