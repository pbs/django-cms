from django.forms import Textarea
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from cms.utils import cms_static_url
from ..settings import CKEDITOR_CONFIG
import json


class CKEditor(Textarea):

    def __init__(self, installed_plugins=None,  **kwargs):
        super(CKEditor, self).__init__(**kwargs)
        self.installed_plugins = installed_plugins

    class Media:
        js = [cms_static_url(path) for path in (
            'ckeditor/ckeditor.js',
            'ckeditor/adapters/jquery.js',
            'js/placeholder_editor_registry.js',
            'js/ckeditor.placeholdereditor.js',
        )]

    def render_editor(self, name, value, attrs=None):
        return super(CKEditor, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        context = {
            'name': name,
            'installed_plugins': self.installed_plugins,
            'controls_css': cms_static_url('css/tinymce.plugin_controls.css'),
            'ck_config': json.dumps(CKEDITOR_CONFIG)
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/ckeditor.html', context))

    def render(self, name, value, attrs=None):
        return self.render_editor(name, value, attrs) + \
            self.render_additions(name, value, attrs)
