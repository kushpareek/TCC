from django import template
from ..models import UserVideoStatus

register = template.Library()

@register.filter
def get_item(queryset, video_id):
    try:
        # Retrieve the UserVideoStatus object based on video_id
        user_video_status = queryset.get(video__id=video_id)
        # Check if the user has paid for the video
        if user_video_status.has_paid:
            return user_video_status
        else:
            return None  # Return None if the user hasn't paid
    except UserVideoStatus.DoesNotExist:
        return None