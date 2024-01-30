from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home),
    path("register/", views.RegistrationAPIView.as_view(), name="register"),
    path("login/", views.LoginAPIView.as_view(), name="login"),
    path("logout/", views.LogoutAPIView.as_view(), name="logout"),
    path("publish/", views.PublishPostAPIView.as_view(), name="publish_post"),
    path("react/", views.ReactPostAPIView.as_view(), name="react_post"),
]
