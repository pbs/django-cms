import re 

from django import template
register = template.Library()

@register.filter
def decode_iframe (string):
    iframe_start = re.compile("&lt;iframe", re.IGNORECASE)
    iframe_end = re.compile("&gt;&lt;/iframe&gt;", re.IGNORECASE)
    string = iframe_start.sub("<iframe", string)
    string = iframe_end.sub("></iframe>", string)
    return string