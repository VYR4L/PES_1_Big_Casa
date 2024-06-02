from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('login-manager/', views.LoginManager.as_view(), name='login_manager'),
    path('manage-users/', views.ManageUsers.as_view(), name='manage_users'),
    path('manage-user/<int:pk>/', views.ManageUsers.as_view(), name='manage_user'),
    path('users-annual-leave/', views.ManagerAnnualLeave.as_view(), name='users_annual_leave'),
    path('user-annual-leave/<int:pk>/', views.ManagerAnnualLeave.as_view(), name='user_annual_leave'),
]
