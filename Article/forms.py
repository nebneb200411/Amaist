from django import forms
from django.forms.widgets import TextInput
from .models import Article, Tag
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content',)  # 'tag')
        widgets = {
            'content': SummernoteWidget(),
            'title': forms.TextInput(attrs={'class': 'title'}),
            # 'tag': forms.TextInput(attrs={'class': 'tag', 'name': 'tag'}),
        }


"""
TagInlineFormSet = forms.inlineformset_factory(
    Article, Article.tag.through, form=ArticleForm, fields='__all__', can_delete=False, extra=5, max_num=10
)
"""
