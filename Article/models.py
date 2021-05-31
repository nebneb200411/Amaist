from django.db import models
from django.contrib.auth import get_user_model

# ユーザー名取得
User = get_user_model()


class Tag(models.Model):
    tag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE)
    content = models.TextField('テキスト')
    title = models.TextField('タイトル', max_length=50)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    good_from = models.ManyToManyField(
        User, related_name="good_from", default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'


class Comment(models.Model):
    comment_to = models.OneToOneField(
        Article, related_name="comment_to", on_delete=models.CASCADE, default=None)
    response_from = models.OneToOneField(
        User, related_name="response_from", on_delete=models.CASCADE)
    response_to = models.ManyToManyField(
        User, related_name="response_to", default=None, null=True)
    comment = models.TextField('コメント', max_length=1000, null=False)
    created_at = models.DateTimeField('コメント日時', auto_now_add=True)
    good = models.IntegerField('いいねの数', default=0)  # 誰がいいねしたかは表示しない．数だけ数える

    def __str__(self):
        return self.response_from

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'
# マイグレーションはまだしない．
