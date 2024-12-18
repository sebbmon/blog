from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),  # Rejestracja
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='/'), name='login'),  # Logowanie
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Wylogowanie
]