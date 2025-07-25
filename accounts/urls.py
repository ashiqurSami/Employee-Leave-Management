from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/',views.register_view, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='home'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('profile/',views.profile_view,name='profile'),
path('login-redirect/', views.login_redirect_view, name='login_redirect')
]