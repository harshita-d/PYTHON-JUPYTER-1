from django.urls import path, include
from loginapp import views

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("signin/", views.SignUpView.as_view(), name="signin"),
]
