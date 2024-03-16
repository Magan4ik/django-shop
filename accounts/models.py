from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import UserManager
from accounts.validators import validate_username, validate_name


class User(AbstractUser):
    username = models.CharField(max_length=50,
                                unique=True,
                                validators=[validate_username])
    email = models.EmailField(unique=True,
                              max_length=255)
    first_name = models.CharField(max_length=50,
                                  validators=[validate_name])
    last_name = models.CharField(max_length=50,
                                 validators=[validate_name])

    address = models.CharField(max_length=100)

    register_token = models.CharField(max_length=16, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'address']

    objects = UserManager()

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()
        self.username = self.username.lower()
        super().save(*args, **kwargs)
