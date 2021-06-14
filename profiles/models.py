from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article
from data_library.models import DataLibrary
from question.models import Question

User = get_user_model()


def icon_path(instance, filename):
    return f'user/{instance.user.id}/icon/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(
        User, related_name="user", on_delete=models.CASCADE)
    following = models.ManyToManyField(
        User, related_name="following", blank=True, default=None)
    follower = models.ManyToManyField(
        User, related_name="follower", blank=True, default=None)
    introduction = models.TextField(max_length=400, blank=True)
    icon = models.ImageField('アイコン', upload_to=icon_path, blank=True)
    articles = models.ForeignKey(
        Article, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)
