from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)
    introduction = models.TextField(
        '自己紹介', max_length=255, unique=True, blank=True)
    icon = models.ImageField('アイコン', upload_to='images', blank=True)
    followees = models.ManyToManyField('User', verbose_name='フォロー中のユーザー',
                                       through='Follow', related_name='+', through_fields=('follower', 'followee'))
    followers = models.ManyToManyField('User', verbose_name='フォローされているユーザー',
                                       through='Follow', related_name='+', through_fields=('followee', 'follower'))
    # articles = models.ForeignKey(
    # 'article.Article', blank=True, on_delete=models.CASCADE, null=True)


class Follow(models.Model):
    follower = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='follower_friendship', null=True)
    followee = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='followee_friendship', null=True)

    class Meta:
        unique_together = ('follower', 'followee')
