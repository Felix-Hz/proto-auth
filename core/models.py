from django.db import models


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Username = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Origin = models.CharField(max_length=10)

    def __str__(self):
        return self.Username


class Session(models.Model):
    SessionID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    LoginTime = models.DateTimeField(auto_now_add=True)
    LogoutTime = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session for {self.UserID} - {self.LoginTime}"
