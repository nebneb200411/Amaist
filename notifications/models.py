from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid


class Notifications(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.TextField('title')
    content = RichTextUploadingField()
    created_at = models.DateTimeField('created at', auto_now_add=True)

    def __str__(self):
        return self.title
