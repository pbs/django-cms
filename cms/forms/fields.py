# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from django.forms.fields import EMPTY_VALUES
from cms.models.pagemodel import Page
from cms.forms.widgets import PageSelectWidget
from cms.forms.utils import get_site_choices, get_page_choices

class SuperLazyIterator(object):
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __iter__(self):
        return iter(self.func())


class LazyChoiceField(forms.ChoiceField):

    def _get_choices(self):
        return self._choices

    def _set_choices(self, value):
        self._choices = self.widget.choices = SuperLazyIterator(value)

    choices = property(_get_choices, _set_choices)



class PageSelectFormField(forms.MultiValueField):
    widget = PageSelectWidget
    default_error_messages = {
        'invalid_site': _(u'Select a valid site'),
        'invalid_page': _(u'Select a valid page'),
    }
    def __init__(self, queryset, empty_label=u"---------", cache_choices=False,
                 required=True, widget=None, to_field_name=None, *args, **kwargs):
        errors = self.default_error_messages.copy()
        if 'error_messages' in kwargs:
            errors.update(kwargs['error_messages'])
        kwargs['required']=required
        fields = (
            LazyChoiceField(choices=get_site_choices, required=False, error_messages={'invalid': errors['invalid_site']}),
            LazyChoiceField(choices=get_page_choices, required=False, error_messages={'invalid': errors['invalid_page']}),
        )
        kwargs.pop('limit_choices_to', None)
        super(PageSelectFormField, self).__init__(fields, *args, **kwargs)

    def compress(self, data_list):
        if data_list:
            page_id = data_list[1]

            if page_id in EMPTY_VALUES:
                if not self.required:
                    return None
                raise forms.ValidationError(self.error_messages['invalid_page'])
            return Page.objects.get(pk=page_id)
        return None


class PlaceholderFormField(forms.Field):
    pass