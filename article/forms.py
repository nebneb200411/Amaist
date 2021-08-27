from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget


class ArticleForm(forms.ModelForm):
    is_published = forms.BooleanField(initial=True, required=False)

    class Meta:
        model = Article
        fields = ('title', 'content', 'is_published',)
        widgets = {
            'content': CKEditorWidget(),
            'title': forms.TextInput(attrs={'class': 'title', 'placeholder': '記事のタイトルを入力してください'}),
        }


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'comment': CKEditorWidget(),
        }
