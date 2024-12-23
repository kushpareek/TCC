# nexus/templatetags/text_filters.py
from django import template
import re
from django.urls import reverse
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def process_mentions(value):
    """
    Converts @username in the text to links to the user's profile.
    """
    pattern = r'@(\w+)'
    
    def replace_match(match):
        username = match.group(1)
        url = reverse('profile', args=[username])
        return f'<a href="{url}">@{username}</a>'
    
    result = re.sub(pattern, replace_match, escape(value))
    return mark_safe(result)
