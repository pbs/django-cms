from django.contrib.sites.models import Site

from admin_extend.extend import registered_modeladmin, extend_registered

from cms.signals import clear_cache_for_sites, with_site_cache_clear_disabled


@extend_registered
class ExtendedSiteAdmin(registered_modeladmin(Site)):

    def delete_model(self, request, obj):
        response = self._delete_model_without_cache_clear(request, obj)
        clear_cache_for_sites([obj.id])
        return response

    @with_site_cache_clear_disabled
    def _delete_model_without_cache_clear(self, request, obj):
        return super(ExtendedSiteAdmin, self).delete_model(request, obj)

    @with_site_cache_clear_disabled
    def _changelist_view_without_cache_clear(self, request, *args, **kwargs):
        return super(ExtendedSiteAdmin, self).changelist_view(request, *args, **kwargs)

    def changelist_view(self, request, *args, **kwargs):
        site_will_be_deleted = request.POST.get('post') and \
                               'delete_selected' in request.POST.get('action')
        if site_will_be_deleted:
            site_ids = [int(site_id_str)
                        for site_id_str in request.POST.getlist('_selected_action')]
            response = self._changelist_view_without_cache_clear(request, *args, **kwargs)
            clear_cache_for_sites(site_ids)
            return response
        else:
            return super(ExtendedSiteAdmin, self).changelist_view(request, *args, **kwargs)
