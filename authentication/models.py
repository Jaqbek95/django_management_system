from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    nick = models.CharField(max_length=3)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nick']

    objects = UserManager()

    def __str__(self):
        return self.nick