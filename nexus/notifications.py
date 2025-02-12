from .models import Notification
from django.contrib.auth.models import AnonymousUser

def notifications_count_processor(request):
    """
    Returns a 'notifications_count' variable for any authenticated user.
    """
    if request.user.is_authenticated:
        return {
            "notifications_count": Notification.objects.filter(
                user=request.user, read=False
            ).count()
        }
    else:
        return {"notifications_count": 0}