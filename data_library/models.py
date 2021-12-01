from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
import os
from .validators import validate_file

User = get_user_model()


class Files(models.Model):
    datalibrary_file = models.FileField(
        upload_to='data_library', null=False, validators=[validate_file])

    def filename(self):
        return os.path.basename(self.datalibrary_file.name)

    def __str__(self):
        return str(self.datalibrary_file.name)

# 2021.12.01タイトルを追加


class DataLibrary(models.Model):
    data_file = models.ManyToManyField(Files, related_name='file')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    introduction = RichTextUploadingField()
    title = models.TextField(blank=False, max_length=250, default="タイトル未設定")
    good = models.ManyToManyField(User, related_name="good", default=None)

    def filename(self):
        return os.path.basename(self.uploader)

    def __str__(self):
        return str(self.uploader)


class CommentToDataLibrary(models.Model):
    content = RichTextUploadingField()
    comment_from = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    comment_to = models.ForeignKey(
        DataLibrary, related_name="comment_to", on_delete=models.CASCADE, default=None)
    response_to = models.ManyToManyField(
        User, related_name="data_library_response_to")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
