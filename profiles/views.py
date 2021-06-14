from django.views.generic import UpdateView, DetailView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from .models import Profile
from question.models import Question
from article.models import Article
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
#import os

User = get_user_model()


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    context_object_name = 'profiles'
    pagenate_by = 20

    def get_queryset(self):
        return Profile.objects.exclude(user=self.request.user)


class UserProfileDetailView(DetailView, LoginRequiredMixin):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        # ログイン中のユーザーのフォロー情報を取得
        login_user_follow_count = my_profile.following.all().count()
        login_user_follower_count = my_profile.follower.all().count()
        context["login_user_follow_count"] = login_user_follow_count
        context["login_user_follower_count"] = login_user_follower_count
        questions = Question.objects.filter(contributor=self.request.user)
        context['questions'] = questions
        articles = Article.objects.filter(author=self.request.user)
        context['articles'] = articles
        return context


class OtherUserProfileView(DetailView):
    model = Profile
    template_name = 'profiles/otheruser_profile.html'

    def get_objects(self, **kwargs):
        pk = self.kwargs.get('pk')
        view_profile = Profile.objects.get(pk=pk)
        return view_profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_object()
        my_profile = Profile.objects.get(user=self.request.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["follow"] = follow
        # ログイン中のユーザーのフォロー情報を取得
        login_user_follow_count = view_profile.following.all().count()
        login_user_follower_count = view_profile.follower.all().count()
        context["login_user_follow_count"] = login_user_follow_count
        context["login_user_follower_count"] = login_user_follower_count
        return context


class UserProfileCreateView(CreateView, LoginRequiredMixin):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/create_userprofile.html'

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, "プロフィールの作成に成功しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "プロフィールの作成に失敗しました")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('article:list')


class UserProfileUpdateView(UpdateView, LoginRequiredMixin):
    model = Profile
    template_name = 'profiles/profile_update.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('article_timeline')

    def form_valid(self, form):
        messages.success(self.request, 'プロフィールの編集に成功しました．')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'プロフィールの編集に失敗しました．')
        return super().form_invalid(form)


def follow_unfollow_view(request):
    if request.method == 'POST':
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)
        follower_list = my_profile.following.all()
        # this process will add user to following
        if obj.user in follower_list:
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        # this process will add user to follower
        following_list = obj.follower.all()
        if my_profile.user in following_list:
            obj.follower.remove(my_profile.user)
        else:
            obj.follower.add(my_profile.user)

        # request.META.get('HTTP_REFERER')
        return redirect('profiles:profile_list')
    return redirect('profiles:profile_list')


def profile_not_found(request):
    if request.method == 'GET':
        if Profile.objects.filter(user=request.user).exists():
            my_profile = Profile.objects.get(user=request.user)
            pk = my_profile.pk
            return redirect('profiles:profile_detail', pk=pk)
        else:
            redirect('profiles:profile_create')

    return redirect('profiles:profile_create')
