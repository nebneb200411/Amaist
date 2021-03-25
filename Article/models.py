from django.db import models
from django.contrib.auth import get_user_model


# ユーザー名取得
User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField('テキスト')
    title = models.TextField('タイトル', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'
