from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth import get_user_model, password_validation
from django import forms
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

# get user model
User = get_user_model()

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class MyPassWordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

class SetPasswordForm(SetPasswordForm):
    error_messages = {
        "password_mismatch": "パスワードが一致しませんでした。",
    }
    new_password1 = forms.CharField(
        label = "New password",
        widget = forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class":"form-control",
                }),
        strip=False,
        help_text = password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label = "New password confirmation",
        strip = False,
        widget = forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class":"form-control",
                }),
    )

class MyPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

def activate_user(uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except Exception:
        return False

    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return True

    return False

class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
