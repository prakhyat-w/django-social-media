from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.all_posts, name='all_posts'),
    path('create_post/', views.create_post, name='create_post'),
    path('<int:post_id>/edit_post/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete_post/', views.delete_post, name='delete_post'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
]
