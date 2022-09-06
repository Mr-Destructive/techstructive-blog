import markdown2

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
def convert_markdown(value):
    value = value.replace('<span class="w"><', '<span class="w"><br><')
    return markdown2.markdown(value, extras=['fenced-code-blocks'])#'fenced_code','extra','codehilite', 'fenced-code-blocks'])
