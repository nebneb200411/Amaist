from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Notifications(models.Model):
    title = models.TextField('title')
    content = RichTextUploadingField()
    created_at = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.title
