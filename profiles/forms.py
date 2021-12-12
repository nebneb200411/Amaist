from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('icon', 'introduction')
        widgets = {
            'icon': forms.FileInput(attrs={'class': 'align-self-center'}),
            'introduction': forms.TextInput(attrs={'class': 'align-self-center'}),
        }
