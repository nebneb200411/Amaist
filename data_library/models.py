from django.db import models
from django.contrib.auth import get_user_model
import os

User = get_user_model()


class DataLibrary(models.Model):
    data_file = models.FileField(upload_to='data_library', null=False)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField(max_length=20000, null=True)
    good = models.ManyToManyField(User, related_name="good", default=None)

    def filename(self):
        return os.path.basename(self.data_file.name)

    def __str__(self):
        return str(self.data_file)


class CommentToDataLibrary(models.Model):
    content = models.TextField(max_length=200, null=False)
    comment_from = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    comment_to = models.ForeignKey(
        DataLibrary, related_name="comment_to", on_delete=models.CASCADE, default=None)
    response_to = models.ManyToManyField(
        User, related_name="data_library_response_to")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
