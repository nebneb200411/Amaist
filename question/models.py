from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class QuestionTag(models.Model):
    tag_name = models.TextField(max_length=20)

    def __str__(self):
        return self.tag_name


class Question(models.Model):
    contributor = models.ForeignKey(
        User, related_name="contributor", on_delete=models.CASCADE)
    title = models.TextField(max_length=50)
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    good_from = models.ManyToManyField(User, related_name="commet_good_from")
    tag = models.ManyToManyField(QuestionTag, related_name="question_tag")

    def __str__(self):
        return str(self.contributor)


class CommentToQuestion(models.Model):
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_from = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
    comment_to = models.ForeignKey(
        Question, related_name="comment_to_question", on_delete=models.CASCADE, default=None)
    response_to = models.ManyToManyField(
        User, related_name="comment_response_to")

    def __str__(self):
        return str(self.content)
