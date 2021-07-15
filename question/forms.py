from django import forms
from .models import Question, CommentToQuestion
from ckeditor.widgets import CKEditorWidget


class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'content', )
        widgets = {
            'content': CKEditorWidget(),
            'title': forms.TextInput(attrs={'class': 'title', 'placeholder': '質問のタイトルを入力してください'})
        }


class CommentCreateForm(forms.ModelForm):

    class Meta:
        model = CommentToQuestion
        fields = ('content',)
        widgets = {
            'content': CKEditorWidget(),
        }
