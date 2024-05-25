from django.urls import path

from forbes_list import views

urlpatterns = [path("people/", views.forbesListView.as_view(), name="forbes-list")]
