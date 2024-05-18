from django.urls import path
from .views import movieListView, platformListView

urlpatterns = [path("list/", movieListView), path("platform/", platformListView)]
