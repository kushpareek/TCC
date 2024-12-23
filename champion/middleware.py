from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
from .models import Registration
class PendingApprovalMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Exclude certain paths from redirection
        exempt_paths = [
            reverse('logout'),
            reverse('underreview'),
            # Add paths that should be accessible even when under review
        ]

        # Allow access to admin panel for staff users
        if request.path.startswith('/admin/'):
            return
        if request.path.startswith('/Team_dashboard/'):
            return

        if request.user.is_authenticated:
            try:
                registration = request.user.registration
                if registration.approved == 0:  # 0 corresponds to 'Pending'
                    if request.path not in exempt_paths:
                        return redirect('underreview')
                 # Create this view if needed
            except Registration.DoesNotExist:
                # Handle the case where the user does not have a registration
                # For now, let's log them out
                logout(request)
                return redirect('home')  # Redirect to home or a page where they can register
