from django.urls import path
from .views import movieListView

urlpatterns = [path("list/", movieListView)]
