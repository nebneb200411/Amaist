from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import SignUpForm, activate_user
from django.views.generic import DeleteView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import render
# load templates
# send email

User = get_user_model()


def get_activate_url(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    return "/activate/{}/{}/".format(uid, token)


class SignUpConfirmationView(TemplateView):
    template_name = "registration/signup_confirmation.html"


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('sign_up_confirm')

    def form_valid(self, form, commit=True):
        user = form.save(commit=False)
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
        return render(self.request, 'registration/signup_confirmation.html', {'registered_user': user})


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('login')


class ActivateView(TemplateView):
    template_name = 'registration/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)


class MyPasswordResetView(PasswordResetView):
    subject_template_name = 'registration/password_reset_subject.txt'
