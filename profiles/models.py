from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        User, related_name="following", blank=True)
    follower = models.ManyToManyField(
        User, related_name="follower", blank=True)
    introduction = models.TextField(max_length=400, blank=True)
    icon = models.ImageField('アイコン', upload_to='images', blank=True)
    articles = models.OneToOneField(
        Article, on_delete=models.CASCADE, null=True)
