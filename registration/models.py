from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    introduction = models.TextField(
        '自己紹介', max_length=255, unique=True, blank=True)
