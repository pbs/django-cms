import re 

from django import template
register = template.Library()

@register.filter
def decode_iframe (string): 
    return string.replace("&lt;iframe", "<iframe").replace("&gt;&lt;/iframe&gt;","></iframe>")