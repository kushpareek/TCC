# nexus/templatetags/media_extras.py
from django import template
import os

register = template.Library()

@register.filter
def media_type(url):
    if not url:
        return 'unknown'
    _, ext = os.path.splitext(url.lower())
    ext = ext.strip('.')
    if ext in ['jpg', 'jpeg', 'png', 'gif']:
        return 'image'
    elif ext in ['mp4', 'webm', 'ogg', 'mov']:
        return 'video'
    else:
        return 'unknown'

@register.filter
def file_extension(url):
    if not url:
        return ''
    _, ext = os.path.splitext(url.lower())
    return ext.strip('.')
