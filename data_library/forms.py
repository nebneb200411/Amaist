from django import forms
from .models import DataLibrary


class DataLibraryCreateForm(forms.ModelForm):
    class Meta:
        model = DataLibrary
        fields = ('data_file', 'introduction')
        widgets = {
            'data_file': forms.FileInput(attrs={'class': 'data_file'}),
            'introduction': forms.TextInput(attrs={'class': 'introduction'})
        }
