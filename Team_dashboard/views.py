# dashboard/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from champion.models import Registration  # Adjust as per your app
from .forms import RegistrationForm
from django.core.paginator import Paginator
from django.db.models import Q
from .models import AuditLog
from django.utils import timezone

def is_team_member(user):
    return user.is_authenticated and user.groups.filter(name='Team').exists()

def dashboard_login(request):
    if request.user.is_authenticated:
        return redirect('Team_dashboard:dashboard-home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        print(is_team_member(user))
        if user is not None and is_team_member(user):
            login(request, user)
            return redirect('Team_dashboard:dashboard-home')
        else:
            return render(request, 'Team_dashboard/login.html', {'error': 'Invalid credentials or insufficient permissions.'})
    return render(request, 'Team_dashboard/login.html')

def dashboard_logout(request):
    logout(request)
    return redirect('Team_dashboard:dashboard-login')
@login_required
@user_passes_test(is_team_member)
def dashboard_home(request):
    # Implement logic to gather dashboard statistics
    total_users = Registration.objects.count()
    approved_users = Registration.objects.filter(approved=1).count()
    pending_users = Registration.objects.filter(approved=0).count()
    context = {
        'total_users': total_users,
        'approved_users': approved_users,
        'pending_users': pending_users,
    }
    return render(request, 'Team_dashboard/home.html', context)
@login_required
@user_passes_test(is_team_member)
def user_list(request):
    search_query = request.GET.get('search', '')
    ordering = request.GET.get('ordering', 'user__username')
    users = Registration.objects.filter(
        Q(user__username__icontains=search_query) |
        Q(phone__icontains=search_query) |
        Q(user__email__icontains=search_query)
    ).order_by(ordering)
    paginator = Paginator(users, 10)  # 10 users per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Team_dashboard/user_list.html', {'page_obj': page_obj, 'search_query': search_query})

@login_required
@user_passes_test(is_team_member)
def user_detail(request, pk):
    user = get_object_or_404(Registration, pk=pk)
    return render(request, 'Team_dashboard/user_detail.html', {'user': user})

@login_required
@user_passes_test(is_team_member)
def user_approve(request, pk):
    user = get_object_or_404(Registration, pk=pk)
    user.approved = 1  # Approved
    user.save()
    AuditLog.objects.create(
        user=request.user,
        action=f"Approved user {user.user.username}",
        timestamp=timezone.now()
    )
    return redirect('Team_dashboard:user-detail', pk=pk)

@login_required
@user_passes_test(is_team_member)
def user_reject(request, pk):
    user = get_object_or_404(Registration, pk=pk)
    user.approved = 2  # Rejected
    user.save()
    AuditLog.objects.create(
        user=request.user,
        action=f"Rejected user {user.user.username}",
        timestamp=timezone.now()
    )
    return redirect('Team_dashboard:user-detail', pk=pk)

@login_required
@user_passes_test(is_team_member)
def user_edit(request, pk):
    user_instance = get_object_or_404(Registration, pk=pk)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user_instance)
        if form.is_valid():
            form.save()
            AuditLog.objects.create(
                user=request.user,
                action=f"Edited user {user_instance.user.username}",
                timestamp=timezone.now()
            )
            return redirect('Team_dashboard:user-detail', pk=pk)
    else:
        form = RegistrationForm(instance=user_instance)
    return render(request, 'Team_dashboard/user_edit.html', {'form': form, 'user': user_instance})
@login_required
@user_passes_test(is_team_member)
def audit_log(request):
    logs = AuditLog.objects.all().order_by('-timestamp')
    paginator = Paginator(logs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'Team_dashboard/audit_log.html', {'page_obj': page_obj})
from champion.utils import send_email 
from django.conf import settings
from django.urls import reverse

@login_required
@user_passes_test(is_team_member) # Adjust the login URL as needed
def send_approval_email(request, pk):
    user_registration = get_object_or_404(Registration, pk=pk)
    print(user_registration.user.email)
    if user_registration.approved == 1:
        activation_url = request.build_absolute_uri(reverse('champions_dashboard'))
        html_message = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Membership Approval - The Champions Club</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: 'Montserrat', sans-serif;
            background-color: #000;
            color: #333;
            margin: 0;
            padding: 20px;
        }}
        .email-container {{
            background-color: #000;
            padding: 20px;
            border-radius: 8px;
            max-width: 600px;
            margin: auto;
        }}
        .email-header {{
            text-align: center;
            background-color: #333;
            padding: 20px;
            color: #ffffff;
            border-radius: 8px 8px 0 0;
        }}
        .email-header h1 {{
            font-size: 24px;
            margin: 0;
        }}
        .email-body {{
            padding: 20px;
            background-color: #fff;
            color: #333;
        }}
        .email-body h2 {{
            color: #ffcc00;
            margin-top: 0;
        }}
        .email-body p {{
            line-height: 1.6;
            font-size: 16px;
        }}
        .email-body ol, .email-body ul {{
            margin-left: 20px;
            font-size: 16px;
        }}
        .email-body li {{
            margin-bottom: 10px;
        }}
        .email-button {{
            text-align: center;
            margin-top: 20px;
        }}
        .email-button a {{
            background-color: #ffcc00;
            color: #000;
            padding: 12px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
        }}
        .email-footer {{
            text-align: center;
            padding: 20px;
            background-color: #333;
            color: #fff;
            border-radius: 0 0 8px 8px;
        }}
        .email-footer p {{
            margin: 0;
            font-size: 14px;
        }}
        .email-signature {{
            margin-top: 40px;
        }}
        a {{
            color: #ffcc00;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <div class="email-container">
        <div class="email-header">
            <h1>Membership Approved!</h1>
        </div>
        <div class="email-body">
            <h2>Dear {user_registration.user.first_name},</h2>
            <p>
                We are delighted to inform you that your application to join <strong>The Champions Club</strong> has been approved. Your remarkable achievements and esteemed reputation make you a valued addition to our exclusive community.
            </p>
            <p>
                To finalize your membership, please complete the following steps:
            </p>
            <ol>
                <li><strong>Complete Your Member Profile:</strong> Provide additional details to personalize your experience within our network.</li>
                <li><strong>Activate Your Membership:</strong> Submit your membership subscription fee to unlock full access to all the privileges and benefits we offer.</li>
            </ol>
            <p>
                To proceed, please click the button below:
            </p>
            <div class="email-button">
                <a href="{activation_url}">Finalize Your Membership</a>
            </div>
            <p>
                By completing your registration, you will gain immediate access to:
            </p>
            <ul>
                <li><strong>Exclusive Events:</strong> Invitations to private gatherings, conferences, and networking opportunities with global leaders.</li>
                <li><strong>Elite Network Access:</strong> Connect with a curated group of peers who share your vision and level of accomplishment.</li>
                <li><strong>Premium Services:</strong> Enjoy bespoke experiences and personalized services tailored to your interests.</li>
            </ul>
            <p>
                We are confident that your participation will enrich our community and provide you with unparalleled opportunities for growth and connection.
            </p>
            <p>
                Should you have any questions or require assistance, please do not hesitate to contact our dedicated membership team at <a href="mailto:support@thechampionsclub.com">Support@thechampionsclub.com</a> .
            </p>
            <p>
                Welcome to The Champions Club. We look forward to your active participation.
            </p>
            <p class="email-signature">
                Warm regards,<br><br>
                Shagun Kalash<br>
                Founder & CEO.<br>
                The Champions Club
            </p>
        </div>
        <div class="email-footer">
            <p style="margin-top: 20px; font-size: 12px;">
                *This email and any attachments are confidential and intended solely for the use of the individual or entity to whom they are addressed.*
            </p>
        </div>
    </div>
</body>
</html>
"""

        send_email(
                subject="Membership Approved",
                body=html_message,
                to_email=user_registration.user.email,
                from_email=settings.DEFAULT_FROM_EMAIL
            )
        
            
        
    else:
        print(request, 'Cannot send approval email. The user is not approved.')
    return redirect('Team_dashboard:user-detail', pk=pk)