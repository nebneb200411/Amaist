from django.db import models
from django.contrib.auth import get_user_model
from article.models import Article

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(
        User, related_name="following", blank=True, default=None)
    follower = models.ManyToManyField(
        User, related_name="follower", blank=True, default=None)
    introduction = models.TextField(max_length=400, blank=True)
    icon = models.ImageField('アイコン', upload_to='images', blank=True)
    articles = models.OneToOneField(
        Article, on_delete=models.CASCADE, null=True)

    def profile_posts(self):
        return self.post_set.all()

    def __str__(self):
        return str(self.user.username)
