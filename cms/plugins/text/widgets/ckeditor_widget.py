from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django import forms
from cms.utils import cms_static_url
from ckeditor.widgets import CKEditorWidget


class CKEditor(CKEditorWidget):

    def __init__(self, installed_plugins=None,  **kwargs):
        super(CKEditor, self).__init__(**kwargs)
        self.installed_plugins = installed_plugins

    @property
    def media(self):
        js = [cms_static_url(path) for path in (
            'js/placeholder_editor_registry.js',
            'js/ckeditor.placeholdereditor.js',
        )]
        js += [script for script in CKEditorWidget.Media.js]
        js += [cms_static_url('js/ckeditor.jquery.patch.js')]
        media = forms.Media(js=js)
        return media

    def render_editor(self, name, value, attrs=None):
        return super(CKEditor, self).render(name, value, attrs)

    def render_additions(self, name, value, attrs=None):
        context = {
            'name': name,
            'installed_plugins': self.installed_plugins,
            'controls_css': cms_static_url('css/tinymce.plugin_controls.css')
        }
        return mark_safe(render_to_string(
            'cms/plugins/widgets/ckeditor.html', context))

    def render(self, name, value, attrs=None):
        return self.render_editor(name, value, attrs) + \
            self.render_additions(name, value, attrs)
