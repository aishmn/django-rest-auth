# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from account.managers import CustomUserManager

# Create your models here.


class User(AbstractUser):
    email = models.CharField(_('email address'), max_length=250, unique=True)
    first_name = models.CharField(_('first name'), max_length=250)
    last_name = models.CharField(_('last name'), max_length=250)
    password = models.CharField(_('password'), max_length=250)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
