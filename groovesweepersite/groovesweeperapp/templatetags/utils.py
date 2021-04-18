from django import template

register = template.Library()

@register.filter
def dictitem(dictionary, key):
	return getattr(dictionary, key, None)
