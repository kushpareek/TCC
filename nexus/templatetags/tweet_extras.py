# nexus/templatetags/tweet_extras.py
from django import template

register = template.Library()

@register.inclusion_tag('nexus/nexus_home.html', takes_context=True)
def render_tweet(context, tweet, depth=0):
    return {
        'tweet': tweet,
        'depth': depth,
        'request': context['request'],
    }
