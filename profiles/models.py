from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    username = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    icon = models.ImageField(upload_to='images/', null=True, blank=True)
    articles = models.ForeignKey(
        'article.Article', null=True, blank=True, on_delete=models.CASCADE)
    introduction = models.TextField(null=True, blank=True, max_length=250)

    def __str__(self):
        return self.username
