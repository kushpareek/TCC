# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.dashboard_login, name='dashboard-login'),
    path('logout/', views.dashboard_logout, name='dashboard-logout'),
    path('', views.dashboard_home, name='dashboard-home'),
    path('users/', views.user_list, name='user-list'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
    path('users/<int:pk>/approve/', views.user_approve, name='user-approve'),
    path('users/<int:pk>/reject/', views.user_reject, name='user-reject'),
    path('users/<int:pk>/edit/', views.user_edit, name='user-edit'),
    path('audit-log/', views.audit_log, name='audit-log'),
    # Add more URLs as needed
]
