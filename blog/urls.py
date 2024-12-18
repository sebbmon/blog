from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),  # Strona główna bloga
    path('post/<int:id>/', views.post_detail, name='post_detail'),  # Szczegóły posta
    path('new_post/', views.new_post, name='new_post'),  # Dodanie nowego posta
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),  # Profil użytkownika
]
