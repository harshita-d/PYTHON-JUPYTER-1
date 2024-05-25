from django.urls import path
from .views import (
    movieListView,
    platformListView,
    movieListIndexView,
    platformListIndexView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("list/", movieListView, name="movie-list"),
    path("list/<int:pk>", movieListIndexView, name="movie-id-list"),
    path("platform/", platformListView, name="platform-list"),
    path("platform/<int:pk>", platformListIndexView, name="platform-id-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
