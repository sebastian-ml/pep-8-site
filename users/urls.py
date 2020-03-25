from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html'), name='login'
         ),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'
         ),
    path('register/', views.RegisterCreateView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('settings/', views.ProfileUpdateView.as_view(), name='profile-update'),
]