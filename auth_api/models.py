from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from django.conf import settings


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


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        db_table = "post"

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "comment"

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"


class Reaction(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_positive = models.BooleanField(default=True)

    class Meta:
        db_table = "reaction"

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
