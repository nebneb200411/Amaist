from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .forms import activate_user
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, ListView
from .models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.contrib import messages
from article.models import Article

# SigUpのためのViewを作成


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ActivateView(TemplateView):
    template_name = 'registration/activate.html'

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)

# ユーザー削除のビュー


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('login')


class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    template_name = 'profile/profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールの編集に成功しました．')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'プロフィールの編集に失敗しました．')
        return super().form_invalid(form)


class ArticleListView(ListView, LoginRequiredMixin):
    model = Article
    pagenate_by = 5
    template_name = 'profile/profile_detail.html'

    def get_queryset(self):
        articles = Article.objects.filter(
            author=self.request.user).order_by('-created_at')
        return articles


class UserProfileDetailView(DetailView, LoginRequiredMixin):
    template_name = 'profile/profile_detail.html'
    pk_url_kwargs = 'id'
    model = User

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
