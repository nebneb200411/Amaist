from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
from .forms import activate_user
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView, ListView
from .models import User, Follow
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProfileForm
from django.contrib import messages
from article.models import Article
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
        context = super().get_context_data(**kwargs)
        context['pk'] = User.objects.filter(pk=self.kwargs.get('pk'))
        return context


class FriendAddView(TemplateView, LoginRequiredMixin):
    template_name = 'profile/other_user_profile.html'
    model = Follow


@login_required
def follow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.user.username)
        followee = User.objects.get(username=kwargs['username'])

    except User.DoesNotExist:
        messages.warning(request, '{}は存在しません'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('index'))

    if follower == followee:
        messages.warning(request, '自分自身はフォローできません')

    else:
        _, created = Follow.objects.get_or_create(
            follower=follower, followee=followee)

        if (created):
            messages.success(
                request, 'あなたはすでに{}をフォローしています'.format(followee.username))
        else:
            messages.warning(
                request, 'あなたはすでに{}をフォローしています'.format(followee.username))

    return HttpResponseRedirect(reverse_lazy('index'), kwargs={'username': followee.username})


@login_required
def unfollow_view(request, *args, **kwargs):
    try:
        follower = User.objects.get(username=request.username)
        followee = User.objects.get(username=request.username)
        if follower == followee:
            messages.warning('自分自身のフォローははずせません')
        else:
            unfollow = Follow.objects.get(follower=follower, followee=followee)
            unfollow.delete()
            messages.success(
                request, '{}のフォローを外しました'.format(followee.username))
    except User.DoesNotExist:
        messages.warning(request, '{}は存在しません'.format(kwargs['username']))
        return HttpResponseRedirect(reverse_lazy('index'))

    return HttpResponseRedirect(reverse_lazy('index'), kwargs={'username': followee.username})
