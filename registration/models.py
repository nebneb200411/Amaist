from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    introduction = models.TextField(
        '自己紹介', max_length=255, unique=True, blank=True)
    icon = models.ImageField('アイコン', upload_to='images', blank=True)
    # articles = models.ForeignKey(
    # 'article.Article', blank=True, on_delete=models.CASCADE, null=True)
