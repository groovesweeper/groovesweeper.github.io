from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(needs_autoescape=True)
@stringfilter
def highlight(value, explicit_terms, autoescape=True):
    result = value
    for term in explicit_terms:
    	result = result.replace(term, "<span class='highlight'>%s</span>" % term)
    return mark_safe(result)
