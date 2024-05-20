from django.urls import path
from .views import (
    movieListView,
    platformListView,
    movieListIndexView,
    platformListIndexView,
)

urlpatterns = [
    path("list/", movieListView, name="movie-list"),
    path("list/<int:pk>", movieListIndexView, name="movie-id-list"),
    path("platform/", platformListView, name="platform-list"),
    path("platform/<int:pk>", platformListIndexView, name="platform-id-list"),
]
