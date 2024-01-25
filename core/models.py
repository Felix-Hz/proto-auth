from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    Origin = models.CharField(max_length=10)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_set"
    )

    def __str__(self):
        return self.username


class Session(models.Model):
    SessionID = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    LoginTime = models.DateTimeField(auto_now_add=True)
    LogoutTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.user} - {self.LoginTime}"
