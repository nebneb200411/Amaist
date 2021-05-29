from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views.generic import DeleteView
from django.contrib.auth import get_user_model

User = get_user_model()


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('login')
