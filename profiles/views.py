from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages

# ユーザープロフィールの編集


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'registration/index.html'
    model = Profile

    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()  # すべてのプロフィールデータを取得
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]


class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('index', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールの編集に成功しました．')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'プロフィールの編集に失敗しました．')
        return super().form_invalid(form)
