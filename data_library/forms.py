from django import forms
from .models import DataLibrary, CommentToDataLibrary
from ckeditor.widgets import CKEditorWidget


class DataLibraryCreateForm(forms.ModelForm):
    class Meta:
        model = DataLibrary
        fields = ('introduction', )

        widgets = {
            'introduction': CKEditorWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentToDataLibrary
        fields = ('content',)
        widgets = {
            'content': CKEditorWidget(),
        }
