from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget

GENRE_CHOICES = (
    ('1', '機械学習'), ('2', '確率統計'), ('3', 'AI'), ('4', 'その他')
)


class ArticleForm(forms.ModelForm):
    is_published = forms.BooleanField(initial=True, required=False)
    genre = forms.MultipleChoiceField(choices=GENRE_CHOICES)

    class Meta:
        model = Article
        fields = ('title', 'content', 'genre', 'is_published', )
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
