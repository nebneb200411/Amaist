from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django import forms
# load templates
from django.template.loader import render_to_string
# send email
from django.core.mail import send_mail

# get user model
User = get_user_model()


def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return str(settings.BASE_DIR) + "/activate/{}/{}/".format(uid, token)


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            activate_url = get_activate_url(user)
            subject = "ユーザー登録について"
            context = {
                "username": user.username,
                "email": user.email,
                "register_link": activate_url,
            }
            message = render_to_string('email/register.txt', context)
            user.email_user(subject, message)
        return user

# ユーザー有効化の設定


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
