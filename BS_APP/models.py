from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


from .managers import CustomUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    current_balance = models.IntegerField( null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.full_name

class Transaction(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='sender_name')
    recipient = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='receiver_name')
    amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=200,null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)


