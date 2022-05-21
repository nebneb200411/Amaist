from django import forms
from .models import Article, Comment
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField
from django.conf import settings

class ArticleForm(forms.ModelForm):
    is_published = forms.BooleanField(initial=True, required=False)
    is_published.widget.attrs.update({
                                    'type':'checkbox',
                                    'class' : 'form-check-input',
                                    'id' : 'publish-or-not',
                                    })

    class Meta:
        model = Article
        fields = ('title', 'content', 'is_published', 'genre')
        widgets = {
            'content': CKEditorWidget(attrs={'class':'ckeditor-class'}),
            'title': forms.TextInput(attrs={'class': 'form-control','aria-label':'Sizing example input', 'aria-describedby':'nputGroup-sizing-lg', 'placeholder': '記事のタイトルを入力してください'}),
            'is_published':forms.BooleanField(),
        }
    
    def clean_genre(self):
        genre = self.cleaned_data['genre']
        if not genre in settings.ARTICLE_GENRE_CHOICES.keys():
            raise forms.ValidationError("ジャンルを選択してください")
        return genre
    
    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            raise forms.ValidationError("タイトルを入力してください")
        return title
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if not content:
            raise forms.ValidationError("タイトルを入力してください")
        return content


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment', )
        widgets = {
            'comment': CKEditorWidget(),
        }