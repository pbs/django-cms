# -*- coding: utf-8 -*-
from cms.apphook_pool import apphook_pool
from cms.appresolver import get_app_urls
from cms.utils import get_template_from_request, get_language_from_request
from cms.utils.i18n import get_fallback_languages
from cms.utils.page_resolver import get_page_from_request
from django.conf import settings
from django.conf.urls import patterns
from django.core.urlresolvers import resolve, Resolver404

from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.http import urlquote
from django.contrib.admin.templatetags.admin_static import static
from django.forms.widgets import Media as WidgetsMedia
from django.template.loader import get_template

def _handle_no_page(request, slug):
    if not slug and settings.DEBUG:
        return render_to_response("cms/new.html", RequestContext(request))
    raise Http404('CMS: Page not found for "%s"' % slug)

from cms.models import *

def plugin_to_json(request, plugin_id):
    plugin_id = int(plugin_id)
    print "plugin to json", plugin_id
    plugin = CMSPlugin.objects.get(id=plugin_id)
    data = {
        'plugin_id': plugin_id,
        'snippet_id': plugin.smartsnippetpointer.snippet.id,
    }

    return JsonResponse(data)

def make_media(variables=None):
    media_obj = WidgetsMedia(
        js=((
            static('admin/js/core.js'),
            static('admin/js/admin/RelatedObjectLookups.js'),
            static('libs/jquery-2.1.1.min.js'),
            static('libs/bootstrap/js/bootstrap.min.js'),
            static('admin/js/custom.js'), )
        ),
        css={
            'all': (
                '//fonts.googleapis.com/css?family=Open+Sans:400,300',
                static('libs/bootstrap/css/bootstrap.css'),
                static('libs/ace/css/ace.min.css'),
                static('admin/css/custom.css'), )
        }
    )
    media_obj.add_js(
        (reverse('admin:jsi18n'),
         static('admin/js/SmartSnippetLib.js'),
         static('admin/js/jquery.init.js'),
         static('admin/js/default.jQuery.init.js')))
    from smartsnippets.cms_plugins import variables_media
    variables_media(media_obj, variables)
    return media_obj

def edit_snippet(request, ss_id):
    from smartsnippets.models import *
    snippet = SmartSnippet.objects.get(id=int(ss_id))
    fake_pointer = SmartSnippetPointer(snippet=snippet)
    selected_snippet_vars = snippet.variables.all()
    empty_plugin_vars = [
        Variable(snippet=fake_pointer, snippet_variable=snippet_var)
        for snippet_var in selected_snippet_vars]
    variables = sorted(empty_plugin_vars,
                    key=lambda v: (v.snippet_variable._order, v.snippet_variable.name))
    media = make_media(variables)
    from cms.plugin_rendering import PluginContext
    context = RequestContext(request)
    context.update({
        'is_popup': True,
        'is_popup_var': '_popup',
        'documentation_link': snippet.documentation_link,
        'description': snippet.description,
        'name': snippet.name,
        'plugin': fake_pointer,
        'original': fake_pointer,
        'variables': variables,
        'media': media,
        'current_site': Site.objects.get_current().id,

        'form_url': '',
        'has_file_field': True,
    })
    return render_to_response('smartsnippets/new_edit.html', context)


def render_snippet(request, snippet_id):
                            # {"var_item1":"{\"short_description\":\"adf\",\"title\":\"sadf\",\"url\":\"asdf\"}","item1_short_description":"adf","item1_title":"sadf","item1_url":"asdf","var_item2":"{\"short_description\":\"sadf\",\"title\":\"asdf\"}","item2_short_description":"sadf","item2_title":"asdf","var_item3":"{}","var_item4":"{}","var_item5":"{}","var_item6":"{}","var_item7":"{}"}
    data = request.POST.get('data', var_a)

    from smartsnippets.models import *
    snippet = SmartSnippet.objects.get(id=int(snippet_id))
    fake_pointer = SmartSnippetPointer(snippet=snippet)
    fake_pointer.placeholder_id = 0
    fake_pointer.id = 0
    fake_pointer.pk = 0
    # from django.conf import settings
    # # print settings.TEMPLATES
    # template = get_template("smartsnippets/mock_fe.html",
    #                         using="django")
    # from sekizai.helpers import (
    #     Watcher as sekizai_context_watcher,
    #     get_varname as sekizai_cache_key,
    # )
    # from django.conf import settings
    # import ipdb;ipdb.set_trace() # pylint: disable=C0321
    # req_context = RequestContext(request,
    #                              processors=settings.TEMPLATES[0]['OPTIONS']['context_processors'])
    # print "req_context.dicts[1].keys()", req_context.dicts[1].keys()
    # print "req_context.dicts[2].keys()", req_context.dicts[2].keys()
    # # import ipdb;ipdb.set_trace() # pylint: disable=C0321
    # with req_context.bind_template(template.template):
    #     context = PluginContext(req_context, fake_pointer, None)
    #     context.update(data)
    #     context['request'] = request

    #     # print "edit_snippet context", context
    #     sekizai_differ = sekizai_context_watcher(context)
    #     content = snippet.render(context)
    #     sekizai_diff = sekizai_differ.get_changes()
    #     print "sekizai", sekizai_diff

    # # context2 = RequestContext(request)
    # # sekizai_differ = sekizai_context_watcher(context2)
    # # render_to_response("smartsnippets/test.html", context2)
    # # sekizai_diff = sekizai_differ.get_changes()
    # # print "sekizai", sekizai_diff
    # req_context['snippet'] = content
    # print "context.dicts[1].dicts[1].keys()", context.dicts[1].dicts[1].keys()
    # print "context.dicts[1].dicts[2].keys()", context.dicts[1].dicts[2].keys()
    # print "context.dicts[2].keys()", context.dicts[2].keys()
    # print "req_context.dicts[1].keys()", req_context.dicts[1].keys()
    # print "req_context.dicts[2].keys()", req_context.dicts[2].keys()
    # # print context
    # # return render_to_response("smartsnippets/mock_fe.html", context2)
    # return render_to_response("smartsnippets/mock_fe.html", req_context)

    context = RequestContext(request)
    context['snippet_1'] = data
    context['snippet_1_id'] = snippet_id
    return render_to_response("smartsnippets/mock_fe.html", context)


def details(request, slug):
    """
    The main view of the Django-CMS! Takes a request and a slug, renders the
    page.
    """
    # get the right model
    context = RequestContext(request)
    # Get a Page model object from the request
    page = get_page_from_request(request, use_path=slug)
    if not page:
        return _handle_no_page(request, slug)

    current_language = get_language_from_request(request)

    # Check that the current page is available in the desired (current) language
    available_languages = page.get_languages()

    # We resolve an alternate language for the page if it's not available.
    # Since the "old" details view had an exception for the root page, it is
    # ported here. So no resolution if the slug is ''.
    if (current_language not in available_languages):
        if settings.CMS_LANGUAGE_FALLBACK:
            # If we didn't find the required page in the requested (current)
            # language, let's try to find a suitable fallback in the list of
            # fallback languages (CMS_LANGUAGE_CONF)
            for alt_lang in get_fallback_languages(current_language):
                if alt_lang in available_languages:
                    alt_url = page.get_absolute_url(language=alt_lang, fallback=True)
                    path = '/%s%s' % (alt_lang, alt_url)
                    # In the case where the page is not available in the
                    # preferred language, *redirect* to the fallback page. This
                    # is a design decision (instead of rendering in place)).
                    return HttpResponseRedirect(path)
        # There is a page object we can't find a proper language to render it
        _handle_no_page(request, slug)

    if apphook_pool.get_apphooks():
        # There are apphooks in the pool. Let's see if there is one for the
        # current page
        # since we always have a page at this point, applications_page_check is
        # pointless
        # page = applications_page_check(request, page, slug)
        # Check for apphooks! This time for real!
        app_urls = page.get_application_urls(current_language, False)
        if app_urls:
            app = apphook_pool.get_apphook(app_urls)
            pattern_list = []
            for urlpatterns in get_app_urls(app.urls):
                pattern_list += urlpatterns
            urlpatterns = patterns('', *pattern_list)
            try:
                view, args, kwargs = resolve('/', tuple(urlpatterns))
                return view(request, *args, **kwargs)
            except Resolver404:
                pass

    # Check if the page has a redirect url defined for this language.
    redirect_url = page.get_redirect(language=current_language)
    if redirect_url:
        if (settings.i18n_installed and redirect_url[0] == "/"
            and not redirect_url.startswith('/%s/' % current_language)):
            # add language prefix to url
            redirect_url = "/%s/%s" % (current_language, redirect_url.lstrip("/"))
        # prevent redirect to self
        own_urls = [
            'http%s://%s%s' % ('s' if request.is_secure() else '', request.get_host(), request.path),
            '/%s%s' % (current_language, request.path),
            request.path,
        ]
        if redirect_url not in own_urls:
            return HttpResponseRedirect(redirect_url)

    # permission checks
    if page.login_required and not request.user.is_authenticated():
        if settings.i18n_installed:
            path = urlquote("/%s%s" % (request.LANGUAGE_CODE, request.get_full_path()))
        else:
            path = urlquote(request.get_full_path())
        tup = settings.LOGIN_URL , "next", path
        return HttpResponseRedirect('%s?%s=%s' % tup)

    template_name = get_template_from_request(request, page, no_current_page=True)
    # fill the context
    context['lang'] = current_language
    context['current_page'] = page
    context['has_change_permissions'] = page.has_change_permission(request)
    context['has_view_permissions'] = page.has_view_permission(request)

    if not context['has_view_permissions']:
        return _handle_no_page(request, slug)

    return render_to_response(template_name, context)

var_a = {u'item2': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/RVR_Slide.jpg',
                        u'short_description': u'The first .',
                        u'title': u'River Valley Rhythms',
                        u'url': u'http://www.cetconnect.org/rivervalleyrhythms/'},
             u'item3': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/WallanderSlide.jpg',
                        u'short_description': u'ed, Emmy-nominated series to a poignant end.',
                        u'title': u'Wallander \u2013 The Final Season',
                        u'url': u'http://www.cetconnect.org/featured-programs/wallander-final-season/'},
             u'item1': {u'short_description': u'The 49thl 26 - April 30, 2016',
                        u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/GrantchesterSlideNew.jpg',
                        u'title': u'a'},
             u'item6': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/GrantchesterSlideNew.jpg',
                        u'short_description': u'Rejoin vir.',
                        u'title': u'Grantchester Season Two',
                        u'url': u'http://www.cetconnect.org/featured-programs/grantchester-season-two/'},
             u'item7': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/GrantchesterSlideNew.jpg',
                        u'short_description': u'Rejoin vir.',
                        u'title': u'Grantchester Season Two',
                        u'url': u'http://www.cetconnect.org/featured-programs/grantchester-season-two/'},
             u'item4': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/GrantchesterSlideNew.jpg',
                        u'short_description': u'Rejoin vir.',
                        u'title': u'Grantchester Season Two',
                        u'url': u'http://www.cetconnect.org/featured-programs/grantchester-season-two/'},
             u'item5': {u'image': u'http://pbs.bento.storage.s3.amazonaws.com/hostedbento-prod/filer_public/CET_Images/Programs/GrantchesterSlideNew.jpg',
                        u'short_description': u'Rejoin vir.',
                        u'title': u'Grantchester Season Two',
                        u'url': u'http://www.cetconnect.org/featured-programs/grantchester-season-two/'},
}
