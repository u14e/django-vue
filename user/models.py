from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=250)

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.phone
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    code = models.CharField(max_length=10)
    phone = models.CharField(max_length=30)
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.code
