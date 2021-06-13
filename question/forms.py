from django import forms
from .models import Question
from django_summernote.widgets import SummernoteWidget


class QuestionCreateForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'content', )
        widgets = {
            'content': SummernoteWidget(),
            'title': forms.TextInput(attrs={'class': 'title'})
        }
