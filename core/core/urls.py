from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("movie/", include("home.urls")),
    path("forbes/", include("forbes_list.urls")),
    path("", include("loginapp.urls")),
]
