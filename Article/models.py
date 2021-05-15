from django.db import models
from django.contrib.auth import get_user_model

# ユーザー名取得
User = get_user_model()


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField('テキスト')
    title = models.TextField('タイトル', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    good_count = models.IntegerField('いいねの数', default=0)
    #tags = models.ManyToManyField('タグ', Tag)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'


class Good(models.Model):
    good_to = models.ForeignKey(Article, on_delete=models.CASCADE)
    good_from = models.ForeignKey(User, on_delete=models.CASCADE)
