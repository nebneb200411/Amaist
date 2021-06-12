from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentToDataLibrary(models.Model):
    content = models.TextField(max_length=200, null=False)
    comment_from = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class DataLibrary(models.Model):
    data_file = models.FileField(upload_to='data_library', null=False)
    uploader = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    introduction = models.TextField(max_length=20000, null=True)
    good = models.ManyToManyField(User, related_name="good", default=None)
    comment = models.ManyToManyField(CommentToDataLibrary)

    def __str__(self):
        return str(self.data_file)
