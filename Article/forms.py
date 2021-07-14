from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content',)
        widgets = {
            'content': CKEditorWidget(),
            'title': forms.TextInput(attrs={'class': 'title'}),
        }


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'comment': CKEditorWidget(),
        }
