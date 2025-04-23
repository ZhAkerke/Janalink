from django.urls import path
from . import views
from .views import create_comment, CommentListView, NewsPostDetail

urlpatterns = [
    # JWT auth
    path('register/', views.register_view),
    path('login/', views.login_view),

    # News (CBV)
    path('posts/', views.NewsPostListCreate.as_view()),
    path('posts/<int:pk>/', views.NewsPostDetail.as_view()),

    # Comments (FBV)
    path('comments/', views.create_comment),

    # Posts by category (FBV)
    path('category/<int:category_id>/posts/', views.posts_by_category),

    path('comments/', CommentListView.as_view()),
    path('comments/create/', create_comment),
    path('comments/delete/', NewsPostDetail.as_view())
]

