from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic import DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
# load templates
from django.template.loader import render_to_string
# send email
from django.core.mail import send_mail

User = get_user_model()


def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return "/activate/{}/{}/".format(uid, token)


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form, commit=True):
        user = form.save(commit=False)
        #user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            activate_url = str(
                self.request._current_scheme_host) + get_activate_url(user)
            subject = "ユーザー登録について"
            context = {
                "username": user.username,
                "email": user.email,
                "register_link": activate_url,
            }
            message = render_to_string('email/register.txt', context)
            user.email_user(subject, message)
            return user
        return super().form_valid(form)


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('login')


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


class ActivateView(TemplateView):
    template_name = 'registration/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)


class MyPasswordResetView(PasswordResetView):
    subject_template_name = 'registration/password_reset_subject.txt'
