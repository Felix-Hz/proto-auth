from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    """
    This class extends the default Django user.
    """

    UserID = models.AutoField(primary_key=True)
    Origin = models.CharField(max_length=10)
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(
        Permission, related_name="custom_user_set"
    )

    class Meta:
        app_label = "auth_api"
        db_table = "user"

    def __str__(self):
        return self.username
