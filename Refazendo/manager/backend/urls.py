from django.urls import path
from . import views

app_name = "manager.backend"

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login_user'),
    path('annual-leave/', views.UserAnnualLeave.as_view(), name='user_annual_leave'),
]