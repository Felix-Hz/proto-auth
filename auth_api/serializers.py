from rest_framework import serializers
from .models import User, Session


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("UserID", "username", "email", "password", "Origin")


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("SessionID", "UserID", "LoginTime", "LogoutTime")
