from django.urls import path
from .views import (
    movieListView,
    platformListView,
    movieListIndexView,
    platformListIndexView,
)

urlpatterns = [
    path("list/", movieListView),
    path("list/<int:pk>", movieListIndexView),
    path("platform/", platformListView),
    path("platform/<int:pk>", platformListIndexView),
]
