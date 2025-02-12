from django import template
from nexus.utils import sanitize_tweet_content
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sanitize_tweet(value):
    cleaned = sanitize_tweet_content(value or "")
    return mark_safe(cleaned)  # Mark safe because we just sanitized it

# from django import template
# from nexus.utils import hashtag_linkify

# register = template.Library()

# @register.filter
# def sanitize_tweet(value):
#     return hashtag_linkify(value)
