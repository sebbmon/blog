from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('new_post/', views.new_post, name='new_post'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:author>/', views.profile, name='profile'),
]
