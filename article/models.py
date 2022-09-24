from importlib.metadata import requires
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
# ユーザー名取得
User = get_user_model()


class Tag(models.Model):
    tag_name = models.TextField(max_length=20)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE)
    content = RichTextUploadingField('テキスト', null=False, blank=False)
    title = models.TextField('タイトル', max_length=50)
    genre = models.TextField('genre', max_length=50,
                             default='その他', blank=False, null=False)
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)
    good_from = models.ManyToManyField(
        User, related_name="good_from", default=None)
    tag = models.ManyToManyField(Tag, related_name="tag")
    is_published = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    is_payment = models.BooleanField(default=False, blank=False, null=False)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'


class Comment(models.Model):
    comment_to = models.ForeignKey(
        Article, related_name="comment_to", on_delete=models.CASCADE, default=None)
    response_from = models.ForeignKey(
        User, related_name="response_from", on_delete=models.CASCADE)
    response_to = models.ManyToManyField(
        User, related_name="response_to", default=None)
    comment = RichTextUploadingField()
    created_at = models.DateTimeField('コメント日時', auto_now_add=True)
    good = models.IntegerField('いいねの数', default=0)  # 誰がいいねしたかは表示しない．数だけ数える

    def __str__(self):
        return str(self.comment_to)

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'

class Order(models.Model):
    user = models.ForeignKey(User, related_name="user_order", on_delete=models.DO_NOTHING, default=None)
    customer_id = models.CharField('customer id in PayJP', max_length=100, blank=False, null=False)
    article = models.ForeignKey(Article, related_name='article_ordered', on_delete=models.DO_NOTHING, default=None)
    token_id = models.CharField('token_id', max_length=100, blank=False, null=False)
    ordered_at = models.DateField('date when purchase event occurred', blank=False, null=False, auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

