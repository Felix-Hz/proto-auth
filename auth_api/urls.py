from django.urls import path
from . import views_auth, views_posts

urlpatterns = [
    # Dummy.
    path("", views_auth.api_home),
    # Authenticate, and authorize.
    path("register/", views_auth.RegistrationAPIView.as_view(), name="register"),
    path("login/", views_auth.LoginAPIView.as_view(), name="login"),
    path("logout/", views_auth.LogoutAPIView.as_view(), name="logout"),
    # Posts, and interactions.
    path("publish/", views_posts.PublishPostAPIView.as_view(), name="publish_post"),
    path("react/", views_posts.ReactPostAPIView.as_view(), name="react_post"),
    path("comment/", views_posts.AddCommentAPIView.as_view(), name="comment_post"),
]
