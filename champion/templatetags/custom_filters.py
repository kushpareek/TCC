from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    try:
        return float(value) * arg
    except (ValueError, TypeError):
        return ''
