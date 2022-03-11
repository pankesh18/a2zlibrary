
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.check_auth, name='check_auth'),
    path('login/', auth_views.LoginView.as_view(template_name='manage_user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='manage_user/logout.html'), name='logout'),
    path('register/', views.register, name='user-register'),
    path('profile/', views.profile, name='user-profile'),
    path('error/', views.error, name='error'),
]
