from django.urls import reverse_lazy
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('icon', 'username', 'introduction')
        widgets = {
            'icon': forms.FileInput(attrs={'class': 'icon'}),
            'introduction': forms.TextInput(attrs={'class': 'introduction'}),
            'username': forms.TextInput(attrs={'class': 'username'}),
        }
