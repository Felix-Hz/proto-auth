from .models import Post, Reaction, Comment

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
                title=title, content=content, author=request.user.UserID, image=image
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


class ReactPostAPIView(APIView):
    def post(self, request):
        post_id, reaction_type = (
            request.data.get("post_id"),
            request.data.get("is_positive"),
        )

        if request.user.is_authenticated:
            if post_id:
                reaction_type = bool(reaction_type)

                if reaction_type in [True, False]:
                    # See if the user had already reacted to this post:
                    existing_reaction = Reaction.objects.filter(
                        post_id=post_id, user_id=request.user.UserID
                    ).first()

                    if existing_reaction:
                        # Only update the row if it's a different reaction_type.
                        if existing_reaction.is_positive != reaction_type:
                            existing_reaction.is_positive = reaction_type
                            existing_reaction.save()
                            return Response(
                                {
                                    "message": f"Reaction '{reaction_type}' updated successfully."
                                },
                                status=status.HTTP_200_OK,
                            )
                        else:
                            return Response(
                                {
                                    "message": f"You have already reacted with '{reaction_type}'."
                                },
                                status=status.HTTP_200_OK,
                            )
                    else:
                        # New reaction:
                        Reaction.objects.create(
                            post_id=post_id,
                            user_id=request.user.UserID,
                            is_positive=reaction_type,
                        )
                        return Response(
                            {
                                "message": f"Reaction '{reaction_type}' stored successfully."
                            },
                            status=status.HTTP_201_CREATED,
                        )
                else:
                    return Response(
                        {"error": "The reaction needs a boolean value (0, 1)."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {
                        "error": f"The request lacks necessary information. Received: post_id={post_id}, reaction_type={reaction_type}"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": "You need to sign in to react to a post."},
                status=status.HTTP_401_UNAUTHORIZED,
            )


class AddCommentAPIView(APIView):
    def post(self, request):
        post_id, content = (
            request.data.get("post_id"),
            request.data.get("content"),
        )

        if request.user.is_authenticated:
            if post_id and content:
                post = Post.objects.filter(id=post_id).first()
                if post:
                    comment = Comment.objects.create(
                        post=post, author_id=request.user.UserID, content=content
                    )

                    return Response(
                        {
                            "message": f"Comment added successfully. Request={request.user.UserID}"
                        },
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"error": "The specified post does not exist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"error": "The request lacks necessary information."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response(
                {"error": "You need to sign in to add a comment."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
