from .models import Post

from django.contrib import messages
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, get_user_model, logout


def api_home(request, *args, **kwargs):
    return JsonResponse({"message": "Test response n1."})


class RegistrationAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            User = get_user_model()
            user = User.objects.create_user(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                response_data = {
                    "status": "Registration was successful.",
                    "token": token.key,
                }
                return Response(response_data)

        return Response({"error": "Missing username or password"}, status=400)


class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "status": "Login was successful."})
        else:
            return Response({"error": "Invalid credentials"}, status=401)


class LogoutAPIView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user = request.user

        if user.is_authenticated:
            logout(request)
            if hasattr(user, "auth_token"):
                user.auth_token.delete()
            return Response({"message": "Logout successful"})
        else:
            return Response({"message": "User is already logged out"})


class PublishPostAPIView(APIView):
    def post(self, request):
        title, content = request.data.get("title"), request.data.get("content")
        image = request.data.get("image") if "image" in request.data else None

        if title and content:
            # Check for duplicates:
            existing_post = Post.objects.filter(title=title, content=content).exists()
            if existing_post:
                return Response(
                    {
                        "error": "This post has already been published. We're looking for unique creations."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # If it's unique:
            post = Post.objects.create(
                title=title, content=content, author=request.user, image=image
            )

            return Response(
                {"message": f"Post '{title}' created successfully."},
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                {"error": "Title and content are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
