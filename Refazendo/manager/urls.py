from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path('login-manager/', views.LoginManager.as_view(), name='login_manager'),
    path('manage-users/', views.ManageUsers.as_view(), name='manage_users'),
    path('manage-user/<int:pk>/', views.ManageUsers.as_view(), name='manage_user'),
    path('users-annual-leave/', views.ManagerAnnualLeave.as_view(), name='users_annual_leave'),
    path('user-annual-leave/<int:pk>/', views.ManagerAnnualLeave.as_view(), name='user_annual_leave'),
    path('users-extra-hours/', views.ManagerExtraHours.as_view(), name='users_extra_hours'),
    path('user-extra-hours/<int:pk>/', views.ManagerExtraHours.as_view(), name='user_extra_hours'),
    path('users-day-off/', views.ManagerDayOff.as_view(), name='users_day_off'),
    path('user-day-off/<int:pk>/', views.ManagerDayOff.as_view(), name='user_day_off'),
]
