from django import forms
from .models import DataLibrary, CommentToDataLibrary
from ckeditor.widgets import CKEditorWidget


class DataLibraryCreateForm(forms.ModelForm):
    class Meta:
        model = DataLibrary
        fields = ('data_file', 'introduction')
        widgets = {
            'data_file': forms.FileInput(attrs={'class': 'data_file'}),
            'introduction': forms.TextInput(attrs={'class': 'introduction'})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentToDataLibrary
        fields = ('content',)
        widgets = {
            'content': CKEditorWidget(),
        }
