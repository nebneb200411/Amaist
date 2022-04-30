from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget
from django.conf import settings



class ArticleForm(forms.ModelForm):
    is_published = forms.BooleanField(initial=True, required=False)
    is_published.widget.attrs.update({
                                    'type':'checkbox',
                                    'data-toggle':'toggle',
                                    'data-on':'公開する',
                                    'data-off':'下書き保存',
                                    'data-onstyle':'info',
                                    'data-offstyle':'outline-dark'
                                    })
    #genre = forms.MultipleChoiceField(choices=settings.ARTICLE_GENRE_CHOICES)
    #genre.widget.attrs.update({'class': 'custom-select'})

    class Meta:
        model = Article
        fields = ('title', 'content', 'is_published', )
        widgets = {
            'content': CKEditorWidget(),
            'title': forms.TextInput(attrs={'class': 'form-control','aria-label':'Sizing example input', 'aria-describedby':'nputGroup-sizing-lg', 'placeholder': '記事のタイトルを入力してください'}),
            'is_published':forms.BooleanField(),
        }


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'comment': CKEditorWidget(),
        }
