import bleach

ALLOWED_TAGS = ['a', 'p', 'br']  # For example
ALLOWED_ATTRS = {
    'a': ['href'],
}

def sanitize_tweet_content(html_content):
    """
    Cleans input, allowing only whitelisted tags/attrs. 
    Returns safe HTML or minimal text.
    """
    return bleach.clean(
        html_content,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=True
    )

# import re
# from django.utils.html import escape
# from django.utils.safestring import mark_safe

# HASHTAG_REGEX = re.compile(r'#(\w+)')

# def hashtag_linkify(raw_text):
#     """
#     1) Escape all user input to avoid XSS.
#     2) Replace #Hashtag with a clickable link to /nexus/topic/Hashtag
#        e.g. #myTopic -> <a href="/nexus/topic/myTopic">#myTopic</a>
#     """
#     # 1) Escape to remove all user-supplied HTML. <script>, <a>, etc. become harmless text.
#     safe_text = escape(raw_text or "")

#     # 2) Linkify any hashtags
#     def replacer(match):
#         hashtag = match.group(1)  # 'myTopic'
#         return f'<a href="/nexus/topic/{hashtag}">#{hashtag}</a>'

#     linked_text = HASHTAG_REGEX.sub(replacer, safe_text)

#     # Mark as safe because we only introduced <a> tags
#     return mark_safe(linked_text)