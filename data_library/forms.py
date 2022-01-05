from django import forms
from .models import DataLibrary, CommentToDataLibrary, Files
from ckeditor.widgets import CKEditorWidget


class DataLibraryCreateForm(forms.ModelForm):
    class Meta:
        model = DataLibrary
        fields = ('title', 'introduction', )

        widgets = {
            'title':forms.TextInput(),
            'introduction': CKEditorWidget(), 
        }

class DataForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ('datalibrary_file', )

        widgets = {
            'datalibrary_file':forms.FileInput(), 
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentToDataLibrary
        fields = ('content',)
        widgets = {
            'content': CKEditorWidget(),
        }
