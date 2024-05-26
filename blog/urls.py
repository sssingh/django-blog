from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    home,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", home, name="home"),
    path("posts", BlogListView.as_view(), name="list-posts"),
    path("posts/<str:pk>/", BlogDetailView.as_view(), name="detail-post"),
    path("posts/new", BlogCreateView.as_view(), name="create-post"),
    path("posts/edit/<str:pk>", BlogUpdateView.as_view(), name="edit-post"),
    path("posts/delete/<str:pk>", BlogDeleteView.as_view(), name="delete-post"),
]
