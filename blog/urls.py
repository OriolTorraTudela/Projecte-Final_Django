from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.post_list, name='posts-list'),
    path('posts/<slug:slug>/', views.post_detail, name='posts-detail-page'),
    path('authors/', views.authors_list, name='authors-list'),
    path('authors/<int:author_id>/', views.author_detail, name='author-detail'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<str:tag>/', views.tag_posts, name='tag-posts'),
]
