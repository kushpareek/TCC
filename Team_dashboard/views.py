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
